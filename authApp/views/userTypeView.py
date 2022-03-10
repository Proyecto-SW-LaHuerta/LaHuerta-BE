from rest_framework import generics
from authApp.models.userType import UserType
from authApp.serializers.userTypeSerializer import UserTypeSerializer

# Listar todos los usuarios y crear un usuario
class UserTypeListCreateView(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


# Obtener, actualizar y borrar usuario especifico
class UserTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
