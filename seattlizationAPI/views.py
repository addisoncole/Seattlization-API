from django.shortcuts import render
from rest_framework import generics
from .models import HomelessCount
from .serializers import HomelessCountSerializer

# Create your views here.



class HomelessCountsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = HomelessCount.objects.all()
    serializer_class = HomelessCountSerializer
