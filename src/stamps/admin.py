from django.contrib import admin
from .models import Category, Group, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'image', 'updated')
    search_fields = ('name', 'description')
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)


class GroupAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'category', 'image', 'updated')
    list_per_page = 20
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category')


admin.site.register(Group, GroupAdmin)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'group', 'height', 'width',
                    'image', 'availible', 'price', 'updated')
    list_per_page = 20
    list_editable = ('availible', 'price')
    list_filter = ('group', 'availible', 'price')
    search_fields = ('name', 'description', 'price', 'group')


admin.site.register(Product, ProductAdmin)
