from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstName', 'lastName', 'phoneNumber', 'birthday', 'email', 'status']
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'phoneNumber': user.phoneNumber,
            'birthday': user.birthday,
            'email': user.email,
            'status': user.status,
        }