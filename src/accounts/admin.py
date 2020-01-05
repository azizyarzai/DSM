from django.contrib import admin
from .models import Profile, Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state',
                    'zip_code', 'country', 'profile')
    list_filter = ('state', 'zip_code', 'country')
    list_per_page = 20


admin.site.register(Address, AddressAdmin)
