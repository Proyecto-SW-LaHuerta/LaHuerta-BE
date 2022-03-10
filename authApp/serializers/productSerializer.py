from rest_framework import serializers
from authApp.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "productId",
            "name",
            "tax",
            "price",
            "stock",
            "categoryId",
        ]
