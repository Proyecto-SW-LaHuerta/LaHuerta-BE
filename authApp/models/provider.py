import uuid
from django.db import models


class Provider(models.Model):
    providerId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(null=False, max_length=45)
    phoneNumber = models.BigIntegerField(null=False)
    offer = models.FloatField(null=False)
    address = models.CharField(null=False, max_length=45)
