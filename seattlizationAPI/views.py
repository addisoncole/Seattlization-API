from django.shortcuts import render
from rest_framework import generics
from .models import HomelessCount, LowIncomeHousing, BuildingPermit, EncampmentRemoval, MFTEProject, CommunitySurvey, CityBudget, HousingMarket
from .serializers import HomelessCountSerializer, HomelessCountDetailSerializer, LowIncomeHousingSerializer, LowIncomeHousingDetailSerializer, BuildingPermitSerializer, EncampmentRemovalSerializer, MFTEProjectSerializer, CommunitySurveySerializer, CommunitySurveyDetailSerializer, CityBudgetSerializer, HousingMarketSerializer

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

class EncampmentRemovalList(generics.ListAPIView):
    queryset = EncampmentRemoval.objects.all()
    serializer_class = EncampmentRemovalSerializer

class MFTEProjectsList(generics.ListAPIView):
    queryset = MFTEProject.objects.all()
    serializer_class = MFTEProjectSerializer

class CommunitySurveysList(generics.ListAPIView):
    queryset = CommunitySurvey.objects.all()
    serializer_class = CommunitySurveySerializer

class CommunitySurveysDetail(generics.RetrieveAPIView):
    queryset = CommunitySurvey.objects.all()
    serializer_class = CommunitySurveyDetailSerializer
    lookup_field = 'year'

class CityBudgetsList(generics.ListAPIView):
    queryset = CityBudget.objects.all()
    serializer_class = CityBudgetSerializer

class HousingMarketsList(generics.ListAPIView):
    queryset = HousingMarket.objects.all()
    serializer_class = HousingMarketSerializer
