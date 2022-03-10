from rest_framework import generics
from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer

# Listar todos los usuarios y crear un usuario
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Obtener, actualizar y borrar usuario especifico
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
