import uuid
from django.db import models


class UserType(models.Model):

    userTypeId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    userType = models.CharField(
        max_length=15,
        choices=(
            ("A", "Administrador"),
            ("N", "Natural"),
        ),
    )
