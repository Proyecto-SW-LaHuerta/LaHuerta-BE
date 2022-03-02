from rest_framework import serializers
from authApp.models.user import User
from authApp.models.bill import Bill
from authApp.serializers.billSerializer import BillSerializer

class UserSerializer(serializers.ModelSerializer):
    bill = BillSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'bill']
    
    def create(self, validated_data):
        billData = validated_data.pop('bill')
        userInstance = User.objects.create(**validated_data)
        Bill.objects.create(user=userInstance, **billData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        bill = Bill.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'bill': {
                        'id': bill.id,
                        'balance': bill.balance,
                        'lastsChangeDate': bill.lastChangeDate,
                        'isActive': bill.isActive
                    }
                }