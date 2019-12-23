from django.contrib import admin
from .models import Category, Group, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'updated')
    prepopulated_fields = {
        'slug': ('name', )
    }
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image', 'updated')
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_per_page = 20
    list_filter = ('category',)


admin.site.register(Group, GroupAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'height', 'width',
                    'image', 'availible', 'price', 'updated')
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_per_page = 20
    list_editable = ('height', 'width', 'availible', 'price')
    list_filter = ('group', 'height', 'width', 'availible', 'price',)


admin.site.register(Product, ProductAdmin)
