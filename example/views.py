from django.shortcuts import render
from rest_framework import generics

from .models import Example
from .serializers import ExampleSerializer

# Create your views here.
class ListExample(generics.ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

class DetailExample(generics.RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
