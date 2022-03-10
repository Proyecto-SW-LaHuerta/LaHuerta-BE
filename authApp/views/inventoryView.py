from rest_framework import generics
from authApp.models.inventory import Inventory
from authApp.serializers.inventorySerializer import Inventoryerializer

# Listar todos los usuarios y crear un usuario
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = Inventoryerializer


# Obtener, actualizar y borrar usuario especifico
class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = Inventoryerializer
