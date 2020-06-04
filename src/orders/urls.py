from django.urls import path
from .views import (
    delivery_address,
    payment,
    success,
    orders,

)

urlpatterns = [
    path('checkout/address/', delivery_address, name="delivery_address"),
    path('checkout/payment/', payment, name="payment"),
    path('checkout/success/<str:order_id>/', success, name="success"),
    path('', orders, name="view_orders"),
]
