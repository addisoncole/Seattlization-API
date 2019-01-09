from django.urls import path

from .views import HomelessCountsList, HomelessCountDetail, LowIncomeHousingList, LowIncomeHousingDetail, BuildingPermitsList, EncampmentRemovalList, MFTEProjectsList, CommunitySurveysList, CommunitySurveysDetail, CityBudgetsList

urlpatterns = [
    path('homelesscounts/', HomelessCountsList.as_view()),
    path('homelesscounts/<int:year>/', HomelessCountDetail.as_view()),
    path('lowincomehousing/', LowIncomeHousingList.as_view()),
    path('lowincomehousing/<int:year>/', LowIncomeHousingDetail.as_view()),
    path('buildingpermits/', BuildingPermitsList.as_view()),
    path('encampmentremovals/', EncampmentRemovalList.as_view()),
    path('mfteprojects/', MFTEProjectsList.as_view()),
    path('communitysurveys/', CommunitySurveysList.as_view()),
    path('communitysurveys/<int:year>/', CommunitySurveysDetail.as_view()),
    path('citybudgets/', CityBudgetsList.as_view()),
    path('', HomelessCountsList.as_view()),
]
