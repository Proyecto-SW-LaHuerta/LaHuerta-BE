from rest_framework import serializers
from authApp.models.paymentType import PaymentType


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            "paymentTypeId",
            "payType",
        ]
