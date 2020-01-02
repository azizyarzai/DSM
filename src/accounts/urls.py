
from django.urls import path
from .views import (
    login,
    register,
    dashboard,
    logout,
    view_profile
)

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name="logout"),
    path('profile/', view_profile, name="view_profile"),
]
