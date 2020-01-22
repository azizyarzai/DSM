from django.urls import path
from .views import (
    delivery_address,
    payment
)

urlpatterns = [
    path('checkout/address/', delivery_address, name="delivery_address"),
    path('checkout/payment/', payment, name="payment"),
]
