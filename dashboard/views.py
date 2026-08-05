from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from products.models import Product
from orders.models import Order
from wishlist.models import Wishlist
from reviews.models import Review


@staff_member_required
def dashboard(request):

    context = {

        "total_users": User.objects.count(),

        "total_products": Product.objects.count(),

        "total_orders": Order.objects.count(),

        "total_reviews": Review.objects.count(),

        "total_wishlist": Wishlist.objects.count(),

        "revenue": sum(order.total_amount for order in Order.objects.all()),

        "recent_orders": Order.objects.order_by("-id")[:5],

        "recent_users": User.objects.order_by("-date_joined")[:5],

        "latest_reviews": Review.objects.select_related(
            "user",
            "product"
        ).order_by("-created_at")[:5],

    }

    return render(
        request,
        "dashboard.html",
        context
    )