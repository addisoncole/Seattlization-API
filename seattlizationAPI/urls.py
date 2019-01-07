from django.urls import path

from .views import HomelessCountsList
from .views import HomelessCountDetail

urlpatterns = [
    path('homelesscounts/', HomelessCountsList.as_view()),
    path('homelesscounts/<int:year>/', HomelessCountDetail.as_view()),
    path('', HomelessCountsList.as_view()),
]
