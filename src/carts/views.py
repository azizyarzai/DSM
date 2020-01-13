from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from stamps.models import Product
from .models import Cart, CartItem

from django.contrib.staticfiles.templatetags.staticfiles import static

from django.conf import settings
import stripe
from razorpay import Client

# Create your views here.


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id=request.session.get('cart_id'))
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
        cart = Cart.objects.get(id=request.session.get('cart_id'))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter = cart_item.quantity
    except ObjectDoesNotExist:
        pass
    template = 'cart/cart.html'
    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
    }
    return render(request, template, context)


# Decreasing item quantity
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(id=request.session.get('cart_id'))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

        # Reducing the amount of the product from the cart
        cart.total = cart.total - product.price
        cart.save()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))


# Removing the full item
def full_remove(request, product_id):
    cart = Cart.objects.get(id=request.session.get('cart_id'))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    # Reducing the amount of the product from the cart
    subtract = cart_item.quantity * product.price
    print(subtract)
    cart.total = cart.total - subtract
    cart.save()

    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))

# Payment


def razorpay(request, total=0):
    key_id = settings.RAZORPAY_KEY_ID
    key_secret = settings.RAZORPAY_KEY_SECRET

    client = Client(auth=(key_id, key_secret))

    try:
        cart = Cart.objects.get(id=request.session.get('cart_id'))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass

    data = {
        "amount": int(total * 100),
        "currency": 'INR',
        "receipt": 'order_rcpid_11',
        "payment_capture": 0,
        "notes": {'Shipping address': 'Bommanahalli, Bangalore'}
    }

    order = client.order.create(data=data)
    order_id = order.get('id')
    print(order_id)
    template = 'cart/razorpay.html'
    context = {
        "order_id": order_id,
        'key_id': key_id
    }
    return render(request, template, context)
