from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added',)
    list_filter = ('date_added',)
    list_per_page = 20


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'active',)
    list_filter = ('product', 'cart',)
    list_editable = ('active',)
    list_per_page = 20


admin.site.register(CartItem, CartItemAdmin)
