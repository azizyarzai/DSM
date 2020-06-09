from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, Http404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from razorpay import Client
from stamps.models import Product
from carts.models import Cart, CartItem, CustomizationData
from orders.models import Order

# Create your views here.


def add_to_cart(request, product_id):
    if request.method == 'GET':
        raise Http404("Page Not Found")
    print(request.POST)

    stamp_body = request.POST.get('stamp_body')
    ink_color = request.POST.get('ink_color')
    special_instruction = request.POST.get('special_instruction')
    line1 = request.POST.get('line1')
    line2 = request.POST.get('line2')
    line3 = request.POST.get('line3')
    line4 = request.POST.get('line4')
    line5 = request.POST.get('line5')
    text = request.POST.get('text')
    top_outer_circle_text = request.POST.get('top_outer_circle_text')
    monogram_initial = request.POST.get('monogram_initial')
    center_text = request.POST.get('center_text')
    bottom_outer_circle_text = request.POST.get('bottom_outer_circle_text')
    below_arrow = request.POST.get('below_arrow')

    if not (line1
            or line2
            or line3
            or line4
            or line5
            or text
            or top_outer_circle_text
            or monogram_initial
            or center_text
            or bottom_outer_circle_text
            or below_arrow
            ):
        raise Http404("Page Not Found")

    customization_data = CustomizationData.objects.create(
        stamp_body=stamp_body,
        line1=line1,
        line2=line2,
        line3=line3,
        line4=line4,
        line5=line5,
        text=text,
        top_outer_circle_text=top_outer_circle_text,
        monogram_initial=monogram_initial,
        center_text=center_text,
        bottom_outer_circle_text=bottom_outer_circle_text,
        below_arrow=below_arrow,
        ink_color=ink_color,
        special_instruction=special_instruction
    )
    customization_data.save()

    product = Product.objects.get(id=product_id)
    cart, cart_created = Cart.objects.new_or_get(request)

    cart_item = CartItem.objects.create(
        product=product,
        quantity=1,
        cart=cart,
        customization_data=customization_data
    )
    cart_item.save()

    return HttpResponseRedirect(reverse_lazy("carts:cart_detail"))


# Removing the full item
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))

# Increasing the quantity of the product


def increase_quantity(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
    except CartItem.DoesNotExist:
        print("DoesNotExist")
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))


# Decreasing item quantity
def decrease_quantity(request, cart_item_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
    except CartItem.DoesNotExist:
        print("DoesNotExist")
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))


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
