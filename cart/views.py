from django.shortcuts import get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import Product
from decimal import Decimal
from django.contrib.auth.decorators import login_required

def get_or_create_cart(request):
    if not request.user.is_authenticated:
        return None

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    return cart

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get the first cart or create one
    cart = get_or_create_cart(request)

    # Check if product already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    item.quantity += 1
    item.save()

    return redirect('/')


def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('/')
def get_cart(request):
    cart = get_or_create_cart(request)

    if cart is None:
        return {
            "cart": None,
            "cart_items": [],
            "cart_total": 0,
            "cart_count": 0,
        }

    items = cart.items.select_related("product")

    total = sum(
        item.product.price * item.quantity
        for item in items
    )

    cart_count = sum(
        item.quantity
        for item in items
    )

    return {
        "cart": cart,
        "cart_items": items,
        "cart_total": total,
        "cart_count": cart_count,
    }
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("/")
