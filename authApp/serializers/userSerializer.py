from rest_framework import serializers
from authApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "userId",
            "first_name",
            "last_name",
            "email",
            "username",
            "is_staff",
            "phoneNumber",
            "birthday",
        ]
