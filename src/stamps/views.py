from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Category, Group, Product

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
    context = {
        "group": group,
        "product": product
    }
    return render(request, template, context)
