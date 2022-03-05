from django.db import models


class Provider(models.Model):
    providerId = models.AutoField(primary_key=True)
