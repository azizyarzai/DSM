from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'created', 'updated', 'checked_out', 'user')
    list_filter = ('created',)
    list_per_page = 20


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity')
    list_filter = ('product',)
    list_per_page = 20


admin.site.register(CartItem, CartItemAdmin)
