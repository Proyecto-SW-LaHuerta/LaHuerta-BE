import uuid
from django.db import models
from .product import Product
from .paymentType import PaymentType
from .user import User


# Bill model definition, attributes and types
class Bill(models.Model):
    billId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    quantity = models.IntegerField(null=False)
    totalPrice = models.BigIntegerField(null=False)
    date = models.DateTimeField()
    userId = models.ForeignKey(
        User,
        related_name="billUserList",
        on_delete=models.SET_NULL,
        null=True,
    )
    productId = models.ForeignKey(
        Product,
        related_name="billProductList",
        on_delete=models.SET_NULL,
        null=True,
    )
    paymentTypeId = models.ForeignKey(
        PaymentType,
        related_name="billPaymentTypeList",
        on_delete=models.SET_NULL,
        null=True,
    )
