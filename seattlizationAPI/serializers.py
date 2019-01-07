from rest_framework import serializers
from .models import HomelessCount

class HomelessCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessCount
        fields = ("year", "total", "unsheltered", "emergency_shelter", "transitional_housing", "number_in_seattle", "pct_female", "pct_male", "pct_trans", "pct_gnc", "pct_white", "pct_black", "pct_latino", "pct_indigenous", "pct_asian", "pct_hawaiian_api", "pct_multiracial")

class HomelessCountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessCount
        fields = ("year", "total", "unsheltered", "emergency_shelter", "transitional_housing", "number_in_seattle", "pct_female", "pct_male", "pct_trans", "pct_gnc", "pct_white", "pct_black", "pct_latino", "pct_indigenous", "pct_asian", "pct_hawaiian_api", "pct_multiracial")
        lookup_field = 'year'
