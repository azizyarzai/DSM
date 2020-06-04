from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from razorpay import Client
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Address
from carts.models import Cart, CartItem
from.models import Order

# Create your views here.


@login_required
def delivery_address(request):
    if request.method == "POST":
        address_id = request.POST.get('address_id')
        print(address_id)
        address = Address.objects.get(id=address_id)
        cart, cart_created = Cart.objects.new_or_get(request)
        order, order_created = Order.objects.get_or_create(cart=cart)
        order.delivery_address = address
        order.save()
        return HttpResponseRedirect(reverse_lazy('orders:payment'))

    else:
        cart, cart_created = Cart.objects.new_or_get(request)
        order, order_created = Order.objects.get_or_create(cart=cart)
        template = 'orders/delivery_address.html'
        context = {
            'order': order
        }
        return render(request, template, context)

# Payment


@login_required
def payment(request, total=0):
    key_id = settings.RAZORPAY_KEY_ID
    key_secret = settings.RAZORPAY_KEY_SECRET

    client = Client(auth=(key_id, key_secret))

    try:
        cart, cart_created = Cart.objects.new_or_get(request)
        cart_items = CartItem.objects.filter(cart=cart)
        order_obj, order_created = Order.objects.get_or_create(cart=cart)
        total = order_obj.total
    except ObjectDoesNotExist:
        pass

    data = {
        "amount": int(total * 100),
        "currency": 'INR',
        "receipt": 'order_rcpid_11',
        "payment_capture": 0,
        "notes": {'Shipping address': str(order_obj.delivery_address)}
    }

    order = client.order.create(data=data)
    order_id = order.get('id')
    template = 'orders/payment.html'

    context = {
        "order_id": order_id,
        'key_id': key_id,
        'order': order_obj,
        'cart_items': cart_items
    }
    return render(request, template, context)


@login_required
def success(request, order_id):
    cart, cart_created = Cart.objects.new_or_get(request)
    order, order_created = Order.objects.get_or_create(cart=cart)
    if order.check_done():
        placed = order.mark_placed()

    if placed:
        cart.checked_out = True
        cart.save()

    template = 'orders/success.html'
    context = {}
    return render(request, template, context)


@login_required
def orders(request):
    orders = Order.objects.all().filter(cart__user=request.user)
    template = 'orders/orders.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)
