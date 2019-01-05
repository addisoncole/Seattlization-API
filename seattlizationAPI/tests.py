from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import HomelessCount
from .serializers import HomelessCountSerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_homeless_count(year="", total="", unsheltered="", emergency_shelter="", transitional_housing="" ):
        if year != "" and total != "":
            HomelessCount.objects.create(year=year, total=total, unsheltered=unsheltered, emergency_shelter=emergency_shelter, transitional_housing=transitional_housing)

    def setUp(self):
        # add test data
        self.create_homeless_count(2015, 10551)
        self.create_homeless_count(2016, 12100)


class GetHomelessCountsTest(BaseViewTest):

    def test_get_homeless_counts(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("homelesscounts")
        )
        # fetch the data from db
        expected = HomelessCount.objects.all()
        serialized = HomelessCountSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
