from django.shortcuts import render
from rest_framework import generics
from .models import HomelessCount, LowIncomeHousing, BuildingPermit
from .serializers import HomelessCountSerializer, HomelessCountDetailSerializer, LowIncomeHousingSerializer, LowIncomeHousingDetailSerializer, BuildingPermitSerializer

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

class BuildingPermitsList(generics.ListAPIView):
    queryset = BuildingPermit.objects.all()
    serializer_class = BuildingPermitSerializer
