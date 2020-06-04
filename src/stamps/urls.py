
from django.urls import path
from .views import (
    browse_stamps,
    category,
    group,
    product
)

urlpatterns = [
    path('browse-stamps/', browse_stamps, name="browse_stamps"),
    path('<slug:slug_category>/', category, name="category"),
    path('<slug:slug_category>/<slug:slug_group>/', group, name="group"),
    path('<slug:slug_category>/<slug:slug_group>/<slug:slug_product>/',
         product, name="product"),
]
