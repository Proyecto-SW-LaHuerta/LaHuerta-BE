from rest_framework import serializers
from authApp.models.bill import Bill


# BillSerializer serializer definition
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = [
            "billId",
            "quantity",
            "totalPrice",
            "date",
            "userId",
            "productId",
            "paymentTypeId",
        ]
