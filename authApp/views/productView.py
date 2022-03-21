from asyncio import exceptions
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ProductPicture(APIView):
    def get(self, request, *args):
        print(str(self.parser_classes))
        return Response({'parsers': ''.join(map(str,self.parser_classes))}, status=204)

class CreateProduct(APIView):
    def post(self, request):
        if 'picture' not in request.data:
            raise exceptions.ParseError('No se ha seleccionado el archivo')

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            validate_data = serializer.validated_data
            product = Product(**validate_data)
            product.save()
            serializer_response = ProductSerializer(product)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


