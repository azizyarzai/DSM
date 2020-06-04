from django.db import models
from stamps.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'wishlist'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return str(self.user)


class WishlistItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, related_name="wishlist_item")
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE, related_name="wishlist_item")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist_item'
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'

    def __str__(self):
        return str(self.product)
