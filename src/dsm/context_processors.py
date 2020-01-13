from cart.models import Cart, CartItem
from stamps.models import Category


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        cart_id = request.session.get("cart_id", None)
        cart = Cart.objects.filter(id=cart_id)
        if cart.count() == 1:
            print("Cart exists")
            cart = cart.first()
            if request.user.is_authenticated and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            cart = Cart.objects.new_cart(user=request.user)
            request.session['cart_id'] = cart.id
            print("New cart created")
        try:
            cart = Cart.objects.filter(id=request.session.get('cart_id'))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += 1
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)


def nav_drop_menu(request):
    categories = Category.objects.all()
    return dict(categories=categories)
