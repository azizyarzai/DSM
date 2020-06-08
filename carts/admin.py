from django.contrib import admin
from .models import Cart, CartItem, CustomizationData
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'created', 'updated', 'checked_out', 'user')
    list_filter = ('created',)
    search_fields = ('id', 'user')
    list_per_page = 20


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'customization_data')
    list_filter = ('cart',)
    search_fields = ('product', 'cart', 'quantity')
    list_per_page = 20


admin.site.register(CartItem, CartItemAdmin)


class CustomizationDataAmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(CustomizationData, CustomizationDataAmin)
