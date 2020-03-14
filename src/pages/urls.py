
from django.urls import path
from .views import (
    home,
    about,
    wish_list

)

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('wishlist/', wish_list, name="view_wish"),
]
