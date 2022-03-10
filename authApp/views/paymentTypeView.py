from rest_framework import generics
from authApp.models.paymentType import PaymentType
from authApp.serializers.paymentTypeSerializer import PaymentTypeSerializer

# Listar todos los usuarios y crear un usuario
class PaymentTypeListCreateView(generics.ListCreateAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


# Obtener, actualizar y borrar usuario especifico
class PaymentTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
