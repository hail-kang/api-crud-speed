from rest_framework import viewsets
from .serializer import DataSerializer, PerformanceSerializer
from .models import Data, Performance

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

import time

class DataViewSet(viewsets.ModelViewSet):
  queryset = Data.objects.all()
  serializer_class = DataSerializer

  def create(self, request, *args, **kwargs):
    start = time.time()

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)

    end = time.time()

    # 측정된 쿼리시간(seconds)을 저장
    Performance.objects.create(name=f"[CREATE] >> 1", performance=(end-start))
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def retrieve(self, request, *args, **kwargs):
    start = time.time()

    instance = self.get_object()
    serializer = self.get_serializer(instance)

    end = time.time()

    # 측정된 쿼리시간(seconds)을 저장
    Performance.objects.create(name=f"[READ] >> 1", performance=(end-start))

    return Response(serializer.data)
    
  def update(self, request, *args, **kwargs):
    start = time.time()

    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
      # If 'prefetch_related' has been applied to a queryset, we need to
      # forcibly invalidate the prefetch cache on the instance.
      instance._prefetched_objects_cache = {}

    end = time.time()

    # 측정된 쿼리시간(seconds)을 저장
    Performance.objects.create(name=f"[UPDATE] >> 1", performance=(end-start))
    return Response(serializer.data)

  def destroy(self, request, *args, **kwargs):
    start = time.time()

    instance = self.get_object()
    self.perform_destroy(instance)

    end = time.time()

    # 측정된 쿼리시간(seconds)을 저장
    Performance.objects.create(name=f"[DELETE] >> 1", performance=(end-start))

    return Response(status=status.HTTP_204_NO_CONTENT)

  
  def list(self, request, *args, **kwargs):
    start = time.time()

    queryset = self.filter_queryset(self.get_queryset())

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)

    end = time.time()
    
    # 측정된 쿼리시간(seconds)을 저장
    Performance.objects.create(name=f"[LIST] >> {queryset.count()}", performance=(end-start))
    return Response(serializer.data)

class PerformanceViewSet(viewsets.ModelViewSet):
  queryset = Performance.objects.all()
  serializer_class = PerformanceSerializer