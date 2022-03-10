from rest_framework import serializers
from authApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "userId",
            "firstName",
            "lastName",
            "phoneNumber",
            "birthday",
            "email",
            "password",
            "userTypeId",
        ]
