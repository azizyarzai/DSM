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


# Decreasing item quantity
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


# Removing the full item
def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('cart:cart_detail'))

# Payment by card to stripe payment gateway


def pay_by_card(request, total=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
    url = static('img/showcase.jpg')
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        payment_intent_data={
            'setup_future_usage': 'off_session',
        },
        line_items=[{
            'name': 'T-shirt',
            'description': 'Comfortable cotton t-shirt',
            'images': [url, ],
            'amount': stripe_total,
            'currency': 'inr',
            'quantity': 1,
        }],
        success_url='https://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://127.0.0.1:8000/cancelled/',
    )

    CHECKOUT_SESSION_ID = session.get('id')
    template = 'cart/pay_by_card.html'
    context = {
        'CHECKOUT_SESSION_ID': CHECKOUT_SESSION_ID,
    }
    return render(request, template, context)


def razorpay(request, total=0):
    key_id = settings.RAZORPAY_KEY_ID
    key_secret = settings.RAZORPAY_KEY_SECRET

    client = Client(auth=(key_id, key_secret))

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
    except ObjectDoesNotExist:
        pass

    data = {
        "amount"           : int(total * 100),
        "currency"         : 'INR',
        "receipt"          : 'order_rcpid_11',
        "payment_capture"  : 0,
        "notes"  : {'Shipping address': 'Bommanahalli, Bangalore'}
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
