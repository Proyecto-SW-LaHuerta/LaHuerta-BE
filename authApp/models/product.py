import uuid
from django.db import models
from .category import Category


class Product(models.Model):
    productId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(null=False, max_length=45)
    tax = models.FloatField(null=False)
    price = models.FloatField(null=False)
    stock = models.IntegerField(null=False)
    categoryId = models.ForeignKey(
        Category,
        related_name="ProductCategoryList",
        on_delete=models.SET_NULL,
        null=True,
    )
