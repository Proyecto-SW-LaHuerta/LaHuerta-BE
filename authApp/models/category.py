import uuid
from itertools import product
from django.db import models


class Category(models.Model):
    categoryId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    categoryType = models.CharField(
        null=False,
        max_length=30,
        choices=(
            ("Nacional", "Nacional"),
            ("Importado", "Importado"),
            ("Verduras_Hortalizas", "Verduras_Hortalizas"),
        ),
    )
    quantity = models.IntegerField(null=False)
