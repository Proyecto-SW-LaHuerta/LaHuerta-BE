from django.db import models
from .user import User

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='bill', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)