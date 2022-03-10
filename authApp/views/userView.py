from rest_framework import generics
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

# Listar todos los usuarios y crear un usuario
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Obtener, actualizar y borrar usuario especifico
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
