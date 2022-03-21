from rest_framework import generics
from authApp.models.bill import Bill
from authApp.serializers.billSerializer import BillSerializer

# Get all bills and post an bill
class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


# Get, update or delete an especific bill
class BillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
