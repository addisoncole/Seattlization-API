from django.shortcuts import render
from rest_framework import generics
from .models import HomelessCount, LowIncomeHousing
from .serializers import HomelessCountSerializer, HomelessCountDetailSerializer
from .serializers import LowIncomeHousingSerializer, LowIncomeHousingDetailSerializer

# Create your views here.

class HomelessCountsList(generics.ListAPIView):
    queryset = HomelessCount.objects.all()
    serializer_class = HomelessCountSerializer

class HomelessCountDetail(generics.RetrieveAPIView):
    queryset = HomelessCount.objects.all()
    serializer_class = HomelessCountDetailSerializer
    lookup_field = 'year'

class LowIncomeHousingList(generics.ListAPIView):
    queryset = LowIncomeHousing.objects.all()
    serializer_class = LowIncomeHousingSerializer

class LowIncomeHousingDetail(generics.ListAPIView):
    queryset = LowIncomeHousing.objects.all()
    serializer_class = LowIncomeHousingSerializer
    lookup_field = 'year'
