from django.shortcuts import render
from django.core.paginator import Paginator

from products.models import Product, Category
from cart.views import get_cart


def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    # Pagination
    paginator = Paginator(products, 6)   # 9 products per page

    page = request.GET.get("page")
    products = paginator.get_page(page)

    context = {
        "products": products,
        "categories": categories,
        "query": query,
        "selected_category": category_id,
    }

    context.update(get_cart(request))

    return render(request, "home.html", context)