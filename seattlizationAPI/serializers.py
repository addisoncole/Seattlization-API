from rest_framework import serializers
from .models import HomelessCount, LowIncomeHousing

class HomelessCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessCount
        fields = ("year", "total", "unsheltered", "emergency_shelter", "transitional_housing", "number_in_seattle", "pct_female", "pct_male", "pct_trans", "pct_gnc", "pct_white", "pct_black", "pct_latino", "pct_indigenous", "pct_asian", "pct_hawaiian_api", "pct_multiracial")

class HomelessCountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomelessCount
        fields = ("year", "total", "unsheltered", "emergency_shelter", "transitional_housing", "number_in_seattle", "pct_female", "pct_male", "pct_trans", "pct_gnc", "pct_white", "pct_black", "pct_latino", "pct_indigenous", "pct_asian", "pct_hawaiian_api", "pct_multiracial")
        lookup_field = 'year'

class LowIncomeHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowIncomeHousing
        fields = ("number_of_units", "year_placed_in_service", "name", "address", "zip_code", "council_district", "hud", "sha", "state_or_county", "wshfc", "city_of_seattle")

class LowIncomeHousingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowIncomeHousing
        fields = ("number_of_units", "year_placed_in_service", "name", "address", "zip_code", "council_district", "hud", "sha", "state_or_county", "wshfc", "city_of_seattle")
        lookup_field = 'year'
