from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    login,
    register,
    logout,
    view_profile,
    add_address,
    update_address,
    delete_address,
    update_personal_details,
    update_accounts_status,
    update_email,
    add_phone,
    change_password
)

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout"),
    path('profile/', view_profile, name="view_profile"),
    path('profile/address/add-address/', add_address, name='add_address'),
    path('profile/address/<int:address_id>/update-address/',
         update_address, name="update_address"),
    path('profile/address/<int:address_id>/delete-address/',
         delete_address, name='delete_address'),
    path('profile/update-personal-details/',
         update_personal_details, name='update-personal-details'),
    path('profile/update-account-status/', update_accounts_status,
         name="update_accounts_status"),
    path('profile/update-email/', update_email, name="update_email"),
    path('profile/add-phone/', add_phone, name="add_phone"),
    path('profile/change-password/', change_password,
         name="change_password"),
]
