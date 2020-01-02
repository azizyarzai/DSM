from django.urls import path
from .views import (
    add_to_cart,
    cart_detail,
    remove_from_cart,
    full_remove,
    pay_by_card,
    razorpay
)

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('', cart_detail, name="cart_detail"),
    path('remove/<int:product_id>/', remove_from_cart, name="remove_from_cart"),
    path('full-remove/<int:product_id>/', full_remove, name="full_remove"),
    path('pay-by-card/', pay_by_card, name="pay_by_card"),
    path('razorpay/', razorpay, name="razorpay"),
]
