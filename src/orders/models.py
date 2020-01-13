from django.db import models
from carts.models import Cart
# Create your models here.


class Order(models.Model):
    billing_profile = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete="DO_NOTHING")

