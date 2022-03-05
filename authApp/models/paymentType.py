from django.db import models


class PaymentType(models.Model):
    paymentTypeId = models.AutoField(primary_key=True)
    payType = models.CharField(max_length=1)
