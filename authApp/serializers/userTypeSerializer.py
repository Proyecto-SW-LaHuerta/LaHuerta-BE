from rest_framework import serializers
from authApp.models.userType import UserType


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = [
            "userTypeId",
            "userType",
        ]
