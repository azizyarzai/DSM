
from django.urls import path, include
from .views import (
    login,
    register,
    dashboard
)

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
]
