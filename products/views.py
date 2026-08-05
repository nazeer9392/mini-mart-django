from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]
    reviews = product.reviews.all()
    average_rating = product.reviews.aggregate(
    Avg("rating")
    )["rating__avg"]

    if average_rating:
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
         "reviews":reviews,
         "average_rating": average_rating,
    })
