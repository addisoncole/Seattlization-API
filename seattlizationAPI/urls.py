from django.urls import path

from .views import HomelessCountsView


urlpatterns = [
    path('homelesscounts/', HomelessCountsView.as_view()),
    path('', HomelessCountsView.as_view()),
]
