from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'total', 'payment_status',
                    'order_status', 'cart')
    list_filter = ('created', 'payment_status', 'order_status')
    list_per_page = 20
    list_editable = ('payment_status', 'order_status')


admin.site.register(Order, OrderAdmin)
