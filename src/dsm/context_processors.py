from carts.models import Cart, CartItem
from stamps.models import Category


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        cart, cart_created = Cart.objects.new_or_get(request)
        print(cart_created)
        try:
            cart_items = CartItem.objects.all().filter(cart=cart)
            for cart_item in cart_items:
                item_count += 1
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)


def nav_drop_menu(request):
    categories = Category.objects.all()
    return dict(categories=categories)
