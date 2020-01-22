from django.urls import path
from .views import (
    add_to_cart,
    cart_detail,
    remove_from_cart,
    full_remove,

)

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('', cart_detail, name="cart_detail"),
    path('remove/<int:product_id>/', remove_from_cart, name="remove_from_cart"),
    path('full-remove/<int:product_id>/', full_remove, name="full_remove"),
]
