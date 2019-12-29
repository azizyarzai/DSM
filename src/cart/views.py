from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from stamps.models import Product
from .models import Cart, CartItem

from django.conf import settings
import stripe


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = None
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return HttpResponseRedirect(reverse_lazy("cart:cart_detail"))


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
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


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('cart:cart_detail'))


def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('cart:cart_detail'))


def checkout(request, cart=None):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(2000 * 100)
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        payment_intent_data={
            'setup_future_usage': 'off_session',
        },
        line_items=[{
            'name': 'T-shirt',
            'description': 'Comfortable cotton t-shirt',
            'images': ['https://example.com/t-shirt.png'],
            'amount': stripe_total,
            'currency': 'inr',
            'quantity': 1,
        }],
        success_url='https://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://127.0.0.1:8000/cart/',
    )

    CHECKOUT_SESSION_ID = session.get('id')
    template = 'cart/checkout.html'
    context = {
        'CHECKOUT_SESSION_ID': CHECKOUT_SESSION_ID,
    }
    return render(request, template, context)
