
from django.urls import path
from .views import (
    browse_stamps
)

urlpatterns = [
    path('browse-stamps/', browse_stamps, name="browse_stamps"),
]
