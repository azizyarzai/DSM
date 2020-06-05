from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'message', 'updated')
    list_filter = ('updated',)
    search_fields = ('subject', 'name', 'email')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
