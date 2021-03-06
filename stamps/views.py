from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Category, Group, Product, DESC_CHOICES


# Create your views here.


def browse_stamps(request):
    template = "stamps/browse_stamps.html"
    context = {}
    return render(request, template, context)


def category(request, slug_category):
    category = get_object_or_404(Category, slug=slug_category)
    groups = Group.objects.filter(category=category)
    template = 'stamps/category.html'
    context = {
        'category': category,
        'groups': groups
    }
    return render(request, template, context)


def group(request, slug_category, slug_group):
    category = get_object_or_404(Category, slug=slug_category)
    group = get_object_or_404(Group, slug=slug_group)
    products = Product.objects.all().filter(group=group)
    template = "stamps/group.html"

    context = {
        "category": category,
        "group": group,
        "products": products
    }
    return render(request, template, context)


def product(request, slug_category, slug_group, slug_product):
    category = get_object_or_404(Category, slug=slug_category)
    group = get_object_or_404(Group, slug=slug_group)
    products = Product.objects.all().filter(group=group)
    product = get_object_or_404(products, slug=slug_product)
    template = "stamps/product.html"

    customization_str = str(product.customization_descriptions)
    cust_arr = customization_str.split(', ')

    cust_d = {}
    for text, val in DESC_CHOICES:
        cust_d[val] = text

    final_customization = {}

    for c in cust_arr:
        final_customization[c] = cust_d.get(c)

    context = {
        "category": category,
        "group": group,
        "product": product,
        "customization_fields": final_customization
    }

    return render(request, template, context)
