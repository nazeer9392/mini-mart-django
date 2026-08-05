from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.views import get_or_create_cart
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related("product")

    if not cart_items.exists():
        return redirect("/")

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = total
            order.save()

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product_name=item.product.name,
                    price=item.product.price,
                    quantity=item.quantity,
                )

            cart_items.delete()

            return redirect("order_success")

    else:
        form = CheckoutForm()

    return render(
        request,
        "checkout.html",
        {
            "form": form,
            "cart_items": cart_items,
            "total": total,
        },
    )
def order_success(request):
    return render(request, "order_success.html")


@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related("items").order_by("-created_at")

    return render(request, "my_orders.html", {
        "orders": orders
    })