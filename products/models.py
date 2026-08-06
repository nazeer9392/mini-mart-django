from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.CharField(max_length=255)

    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# from django.db import models

# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='categories/', blank=True, null=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name='products'
#     )

#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     image = models.ImageField(upload_to='products/')

#     stock = models.PositiveIntegerField(default=0)

#     available = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name