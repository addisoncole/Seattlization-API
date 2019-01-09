from rest_framework import serializers
from .models import HomelessCount, LowIncomeHousing, BuildingPermit, EncampmentRemoval, MFTEProject, CommunitySurvey

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

class  BuildingPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowIncomeHousing
        fields = ( "permit_number", "permit_class", "permit_class_mapped", "permit_type", "permit_type_mapped", "description", "number_of_units", "housing_units_removed", "housing_units_added", "permit_application_date", "permit_approval_date", "permit_completion_date", "location", "link")

class  EncampmentRemovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncampmentRemoval
        fields = ("date", "year", "location", "departments_responsible_for_removal", "vehicle_hazard", "criminal_activity", "waste_and_debris", "health_hazard_to_neighborhood", "limited_emergency_services", "scheduled_worksite", "damage_to_environment", "proximity_to_school_or_elderly")

class  MFTEProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFTEProject
        fields = ("project_name", "tax_exemption_start", "tax_exemption_end", "year_of_approval", "address", "council_district", "targeted_area", "subsidized", "total_units", "total_affordable_units", "microhousing", "SEDU_total", "SEDU_affordable", "studio_units_total", "studio_units_affordable", "one_br_total", "one_br_affordable", "two_br_total", "two_br_affordable", "three_br_total", "three_br_affordable", "four_br_total", "four_br_affordable")

class  CommunitySurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunitySurvey
        fields = ("year", "total_population", "gini_index", "median_income", "income_under_10000", "income_10000_14999", "income_15000_19999", "income_20000_24999", "income_25000_29999", "income_30000_34999", "income_35000_39999", "income_40000_44999", "income_45000_49999", "income_50000_59999", "income_60000_74999", "income_75000_99999", "income_100000_124999", "income_125000_149999", "income_150000_199999", "income_over_200000", "median_rent_studio", "median_rent_1br", "median_rent_2br", "median_rent_3br", "median_rent_4br", "median_rent_5br")

class  CommunitySurveyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunitySurvey
        fields = ("year", "total_population", "gini_index", "median_income", "income_under_10000", "income_10000_14999", "income_15000_19999", "income_20000_24999", "income_25000_29999", "income_30000_34999", "income_35000_39999", "income_40000_44999", "income_45000_49999", "income_50000_59999", "income_60000_74999", "income_75000_99999", "income_100000_124999", "income_125000_149999", "income_150000_199999", "income_over_200000", "median_rent_studio", "median_rent_1br", "median_rent_2br", "median_rent_3br", "median_rent_4br", "median_rent_5br")
        lookup_field = 'year'
