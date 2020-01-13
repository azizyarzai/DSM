from django.db import models
from stamps.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
# Create your models here.


class CartManager(models.Manager):
    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
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
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_item'
        ordering = ('-created',)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)

# Calculating the total of the card


def post_save_cart_item_receiver(sender, instance, *args, **kwarge):
    cart = instance.cart
    total = 0
    cart_items = cart.cart_items.all()
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
    cart.total = total
    cart.save()


post_save.connect(post_save_cart_item_receiver, sender=CartItem)
