from django.urls import path

from .views import HomelessCountsList, HomelessCountDetail
from .views import LowIncomeHousingList, LowIncomeHousingDetail

urlpatterns = [
    path('homelesscounts/', HomelessCountsList.as_view()),
    path('homelesscounts/<int:year>/', HomelessCountDetail.as_view()),
    path('lowincomehousing/', LowIncomeHousingList.as_view()),
    path('lowincomehousing/<int:year>/', LowIncomeHousingDetail.as_view()),
    path('', HomelessCountsList.as_view()),
]
