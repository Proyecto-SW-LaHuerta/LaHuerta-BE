from rest_framework import generics
from authApp.models.provider import Provider
from authApp.serializers.providerSerializer import ProviderSerializer

# Listar todos los usuarios y crear un usuario
class ProviderListCreateView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


# Obtener, actualizar y borrar usuario especifico
class ProviderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
