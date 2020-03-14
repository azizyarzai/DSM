import math
from django.db import models
from django.db.models.signals import pre_save, post_save
from carts.models import Cart
from dsm.utils import unique_order_id_generator
from accounts.models import Address
# Create your models here.

PAYMENT_STATUS = (
    ('paid', 'Paid'),
    ('not paid', 'Not Paid'),
    ('refunded', 'Refunded')
)
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('deliverd', 'Delivered')
)


class OrderManager(models.Manager):
    def all(self):
        return super().all().filter(placed=True)


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    delivery_address = models.ForeignKey(
        Address, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    payment_status = models.CharField(
        max_length=120, default='not paid', choices=PAYMENT_STATUS)
    delivery_charges = models.DecimalField(
        default=0, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    placed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __Str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        delivery_charges = self.delivery_charges
        new_total = math.fsum([cart_total, delivery_charges])
        formated_total = format(new_total, '.2f')
        self.total = formated_total
        self.save()
        return new_total

    def check_done(self):
        delivery_address = self.delivery_address
        total = self.total
        if delivery_address and total > 0:
            return True
        return False

    def mark_placed(self):
        if self.check_done:
            self.placed = True
            self.save()
        return self.placed

# Generate the order id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)


# Generate the order total
def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_save_order, sender=Order)
