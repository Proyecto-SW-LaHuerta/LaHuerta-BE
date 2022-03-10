from rest_framework import serializers
from authApp.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "categoryId",
            "categoryType",
            "quantity",
        ]
