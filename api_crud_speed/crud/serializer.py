from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Data

class DataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Data
    fields = '__all__'