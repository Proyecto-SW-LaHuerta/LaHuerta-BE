from rest_framework import serializers
from authApp.models.inventory import Inventory


class Inventoryerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            "inventoryId",
            "stock",
            "entryDate",
            "providerId",
            "productId",
        ]
