from rest_framework import generics
from authApp.models.category import Category
from authApp.serializers.categorySerializer import CategorySerializer

# Get all categories and post an category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Get, update or delete an especific category
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
