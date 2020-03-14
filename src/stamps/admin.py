from django.contrib import admin
from .models import Category, Group, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'image', 'updated')
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)


class TypeAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'category', 'image', 'updated')
    list_per_page = 20
    list_filter = ('category',)


admin.site.register(Group, TypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'group', 'height', 'width',
                    'image', 'availible', 'price', 'updated')
    list_per_page = 20
    list_editable = ('availible', 'price')
    list_filter = ('group', 'availible', 'price')


admin.site.register(Product, ProductAdmin)
