import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_mart.settings")
django.setup()

from products.models import Product, Category

# Update product images
for product in Product.objects.all():
    if product.image:
        filename = os.path.basename(product.image.name)
        product.image = f"products/{filename}"
        product.save()
        print(f"Updated product: {product.name}")

# Update category images
for category in Category.objects.all():
    if category.image:
        filename = os.path.basename(category.image.name)
        category.image = f"categories/{filename}"
        category.save()
        print(f"Updated category: {category.name}")

print("Done!")