from rest_framework import serializers
from authApp.models.provider import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            "providerId",
            "name",
            "phoneNumber",
            "offer",
            "address",
        ]
