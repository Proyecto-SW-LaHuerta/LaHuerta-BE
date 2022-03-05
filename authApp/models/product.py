from django.db import models


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
