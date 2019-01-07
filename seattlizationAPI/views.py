from django.shortcuts import render
from rest_framework import generics
from .models import HomelessCount
from .serializers import HomelessCountSerializer
from .serializers import HomelessCountDetailSerializer

# Create your views here.

class HomelessCountsList(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = HomelessCount.objects.all()
    serializer_class = HomelessCountSerializer

class HomelessCountDetail(generics.RetrieveAPIView):
    queryset = HomelessCount.objects.all()
    serializer_class = HomelessCountDetailSerializer
    lookup_field = 'year'
