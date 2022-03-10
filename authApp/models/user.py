import uuid
from django.db import models
from .userType import UserType


class User(models.Model):
    userId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    firstName = models.CharField(null=False, max_length=45)
    lastName = models.CharField(null=False, max_length=45)
    phoneNumber = models.BigIntegerField(null=True)
    birthday = models.DateField(null=False)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    password = models.CharField(null=False, max_length=45)
    userTypeId = models.ForeignKey(
        UserType,
        related_name="userTypeList",
        on_delete=models.SET_NULL,
        null=True,
    )
