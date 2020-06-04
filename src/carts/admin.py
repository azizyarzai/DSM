from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'created', 'updated', 'checked_out', 'user')
    list_filter = ('created',)
    search_fields = ('id', 'user')
    list_per_page = 20


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity')
    list_filter = ('cart',)
    search_fields = ('product', 'cart', 'quantity')
    list_per_page = 20


admin.site.register(CartItem, CartItemAdmin)
