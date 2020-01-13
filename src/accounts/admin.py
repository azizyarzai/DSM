from django.contrib import admin
from .models import Profile, Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


COUNTRY_CHOICES = (
    ('', 'Select Country'),
)
STATE_CHOICES = (
    ('', 'Select State'),
)
CITY_CHOICES = (
    ('', 'Select City'),
)


class AddressAdminForm(forms.ModelForm):
    class Meta:
        module = Address
        widgets = {
            'country': forms.Select(attrs={'name': 'country',
                                           'id': 'countryId',
                                           'class': 'countries'
                                           }, choices=COUNTRY_CHOICES),
            'state': forms.Select(attrs={'name': 'state',
                                         'id': 'stateId',
                                         'class': 'states'
                                         }, choices=STATE_CHOICES),
            'city': forms.Select(attrs={'name': 'city',
                                        'id': 'cityId',
                                        'class': 'cities'
                                        }, choices=CITY_CHOICES)
        }


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = ('address', 'city', 'state',
                    'zip_code', 'country', 'user')
    list_filter = ('state', 'zip_code', 'country')
    list_per_page = 20

    # regular stuff
    class Media:
        js = (

            'js/jquery-3.4.1.min.js',  # jquery
            'js/countrystatecity.js',  # geocode
        )


admin.site.register(Address, AddressAdmin)
