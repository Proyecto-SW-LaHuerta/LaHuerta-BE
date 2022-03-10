import uuid
from django.db import models
from .provider import Provider
from .product import Product


class Inventory(models.Model):
    inventoryId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    stock = models.IntegerField(null=False)
    entryDate = models.DateField(null=False)
    providerId = models.ForeignKey(
        Provider,
        related_name="inventoryProviderList",
        on_delete=models.SET_NULL,
        null=True,
    )
    productId = models.ForeignKey(
        Product,
        related_name="inventoryProductList",
        on_delete=models.SET_NULL,
        null=True,
    )
