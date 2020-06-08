from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404
from stamps.models import Category, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

from stamps.models import Product
from .models import Wishlist, WishlistItem
# Create your views here.


def home(request):
    template = "pages/index.html"
    return render(request, template)


def about(request):
    template = "pages/about.html"
    context = {}
    return render(request, template, context)


@login_required
def wishlist(request):
    user_wishlist, wish_created = Wishlist.objects.get_or_create(
        user=request.user)
    wishlist_items = WishlistItem.objects.all().filter(wishlist=user_wishlist)
    print(wishlist_items)
    template = 'pages/wishlist.html'
    context = {
        "wishlist_items": wishlist_items
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_wishlist, wish_created = Wishlist.objects.get_or_create(
        user=request.user)
    wishlist_item, created = WishlistItem.objects.get_or_create(
        product=product,
        wishlist=user_wishlist)
    if created:
        messages.success(
            request, "The product has been added to your wishlist successfully.")
    else:
        messages.error(
            request, "The product is already added to wishlist.")
    group = Group.objects.get(product=product)
    category = Category.objects.get(group=group)
    return HttpResponseRedirect(reverse_lazy("stamps:product", args=[category.slug, group.slug, product.slug]))


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    user_wishlist, wish_created = Wishlist.objects.get_or_create(
        user=request.user)
    try:
        wishlist_item = WishlistItem.objects.get(
            id=wishlist_item_id,
            wishlist=user_wishlist
        )
    except WishlistItem.DoesNotExist:
        return Http404

    wishlist_item.delete()
    messages.success(
        request, "The product has been removed from wishlist successfully.")
    return HttpResponseRedirect(reverse_lazy("pages:wishlist"))
