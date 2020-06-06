from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from razorpay import Client
from stamps.models import Product
from .models import Cart, CartItem
from orders.models import Order
# Create your views here.


def add_to_cart(request, product_id):
    print(request.POST)
    product = Product.objects.get(id=product_id)
    cart, cart_created = Cart.objects.new_or_get(request)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return HttpResponseRedirect(reverse_lazy("carts:cart_detail"))

# View cart details


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart, cart_created = Cart.objects.new_or_get(request)
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter = cart_item.quantity
    except ObjectDoesNotExist:
        pass
    template = 'carts/cart.html'
    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
    }
    return render(request, template, context)


# Decreasing item quantity
def remove_from_cart(request, product_id):
    cart, cart_created = Cart.objects.new_or_get(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))


# Removing the full item
def full_remove(request, product_id):
    cart, cart_created = Cart.objects.new_or_get(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
