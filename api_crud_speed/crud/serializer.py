from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Data, Performance

class DataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Data
    fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Performance
    fields = '__all__'