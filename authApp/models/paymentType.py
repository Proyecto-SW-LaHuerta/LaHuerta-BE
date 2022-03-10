import uuid
from django.db import models


class PaymentType(models.Model):
    paymentTypeId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    payType = models.CharField(
        null=False,
        max_length=15,
        choices=(
            ("E", "Efectivo"),
            ("T", "Tarjeta"),
        ),
    )
