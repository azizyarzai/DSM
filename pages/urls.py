
from django.urls import path
from .views import (
    home,
    about,
    wishlist,
    add_to_wishlist
)

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('wishlist/', wishlist, name="wishlist"),
    path('<int:product_id>/add-to-wishlist/',
         add_to_wishlist, name="add_to_wishlist"),
]
