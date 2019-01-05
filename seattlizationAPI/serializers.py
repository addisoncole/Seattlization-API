from rest_framework import serializers
from .models import HomelessCount


class HomelessCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessCount
        fields = ("year", "total", "unsheltered", "emergency_shelter", "transitional_housing")
