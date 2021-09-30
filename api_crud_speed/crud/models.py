from django.db import models

# Create your models here.

class Data(models.Model):
  name = models.CharField(max_length=100)
  data = models.CharField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  state_code = models.BooleanField(default=False)

class Performance(models.Model):
  name = models.CharField(max_length=100)
  performance = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  state_code = models.BooleanField(default=False)