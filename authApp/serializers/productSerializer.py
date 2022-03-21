from rest_framework import serializers
from authApp.models.product import Product
from drf_extra_fields.fields import Base64ImageField


class ProductSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = [
            "productId",
            "name",
            "tax",
            "price",
            "stock",
            "categoryId",
            "picture",
        ]
