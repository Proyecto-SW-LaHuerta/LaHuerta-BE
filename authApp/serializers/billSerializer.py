from authApp.models.bill import Bill
from rest_framework import serializers

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['balance', 'lastChangeDate', 'isActive']