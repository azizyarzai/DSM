from django.contrib import admin
from .models import Wishlist, WishlistItem
# Register your models here.


class WishlistManager(admin.ModelAdmin):
    list_display = ['user', 'created', 'updated']
    list_per_page = 25
    search_fields = ('user',)


admin.site.register(Wishlist, WishlistManager)


class WishlistItemManager(admin.ModelAdmin):
    list_display = ['product', 'wishlist', 'updated']
    list_per_page = 25
    search_fields = ('product',)


admin.site.register(WishlistItem, WishlistItemManager)
