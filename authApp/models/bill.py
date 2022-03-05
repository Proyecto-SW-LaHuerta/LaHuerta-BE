from django.db import models

from authApp.models.paymentType import PaymentType
from .user import User
from .product import Product
from .paymentType import PaymentType


class Bill(models.Model):
    billId = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    totalPrice = models.BigIntegerField()
    date = models.DateTimeField()
    userId = models.ForeignKey(User, related_name="bill", on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    paymentTypeId = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
