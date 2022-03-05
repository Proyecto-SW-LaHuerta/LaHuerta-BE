from django.db import models


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
