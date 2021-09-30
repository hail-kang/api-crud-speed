from rest_framework import viewsets
from .serializer import DataSerializer, PerformanceSerializer
from .models import Data, Performance

class DataViewSet(viewsets.ModelViewSet):
  queryset = Data.objects.all()
  serializer_class = DataSerializer

class PerformanceiewSet(viewsets.ModelViewSet):
  queryset = Performance.objects.all()
  serializer_class = PerformanceSerializer

