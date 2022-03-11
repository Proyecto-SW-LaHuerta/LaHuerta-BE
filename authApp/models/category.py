import uuid
from django.db import models


# Category model definition, attributes and types
class Category(models.Model):
    categoryId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    categoryType = models.CharField(
        null=False,
        max_length=30,
        choices=(
            ("N", "Nacional"),
            ("I", "Importado"),
            ("V", "Verduras_Hortalizas"),
        ),
    )
    quantity = models.IntegerField(null=False)
