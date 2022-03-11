from rest_framework import serializers
from authApp.models.category import Category


# Category serializer definition
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "categoryId",
            "categoryType",
            "quantity",
        ]
