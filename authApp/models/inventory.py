from django.db import models


class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
