from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(null=False, max_length=100)
    lastName = models.CharField(null=False, max_length=100)
    phoneNumber = models.BigIntegerField(null=True)
    birthday = models.DateField(null=False)
    username = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=254)
