from rest_framework import generics
from authApp.models.category import Category
from authApp.serializers.categorySerializer import CategorySerializer

# Listar todos los usuarios y crear un usuario
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Obtener, actualizar y borrar usuario especifico
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
