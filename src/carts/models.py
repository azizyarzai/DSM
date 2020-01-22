from django.db import models
from stamps.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
# Create your models here.


class CartManager(models.Manager):
    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new_cart(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj


class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    checked_out = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    class Meta:
        db_table = 'cart'
        ordering = ('user',)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, related_name="products")
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_item'
        ordering = ('-created',)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)


# Calculating the total of the cart after saving CartItem
def post_save_cart_item_receiver(sender, instance, *args, **kwarge):
    cart = instance.cart
    total = 0
    cart_items = cart.cart_items.all()
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
    cart.total = total
    cart.save()


post_save.connect(post_save_cart_item_receiver, sender=CartItem)


# Calculating the total of the cart after deleting CartItem
def post_delete_cart_item_receiver(sender, instance, *args, **kwargs):
    cart = instance.cart
    subtract_amount = instance.quantity * instance.product.price
    cart.total = cart.total - subtract_amount
    cart.save()


post_delete.connect(post_delete_cart_item_receiver, sender=CartItem)
