from django.urls import path
from .views import (
    delivery_address,
    payment,
    success_cod,
    success_paid,
    orders,
    cancel_order,
    re_order
)

urlpatterns = [
    path('checkout/address/', delivery_address, name="delivery_address"),
    path('checkout/payment/', payment, name="payment"),
    path('checkout/success-cod/<str:order_id>/',
         success_cod, name="success_cod"),
    path('checkout/success-paid/<str:order_id>/',
         success_paid, name="success_paid"),
    path('', orders, name="view_orders"),
    path('cancel-order/<str:order_id>', cancel_order, name="cancel_order"),
    path('re-order/<str:order_id>', re_order, name="re_order"),
]
