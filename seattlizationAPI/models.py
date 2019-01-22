from django.db import models

#Point in time Count for yearly Count Us In/One Night Count of homeless
class HomelessCount(models.Model):
    year = models.IntegerField(null=False)
    total = models.IntegerField(blank=True, null=True)
    unsheltered = models.IntegerField(blank=True, null=True)
    number_in_shelter_and_transitional_housing = models.IntegerField(blank=True, null=True)
    emergency_shelter = models.IntegerField(blank=True, null=True)
    transitional_housing = models.IntegerField(blank=True, null=True)
    number_unsheltered_in_seattle = models.IntegerField(blank=True, null=True)
    number_sheltered_in_seattle = models.IntegerField(blank=True, null=True)
    number_male_on_street = models.IntegerField(blank=True, null=True)
    number_female_on_street = models.IntegerField(blank=True, null=True)
    number_unknown_gender_on_street = models.IntegerField(blank=True, null=True)
    number_of_minors_on_street = models.IntegerField(blank=True, null=True)
    pct_female = models.IntegerField(blank=True, null=True)
    pct_male = models.IntegerField(blank=True, null=True)
    pct_trans = models.IntegerField(blank=True, null=True)
    pct_gnc = models.IntegerField(blank=True, null=True)
    pct_white = models.IntegerField(blank=True, null=True)
    pct_black = models.IntegerField(blank=True, null=True)
    pct_latino = models.IntegerField(blank=True, null=True)
    pct_indigenous = models.IntegerField(blank=True, null=True)
    pct_asian = models.IntegerField(blank=True, null=True)
    pct_hawaiian_api = models.IntegerField(blank=True, null=True)
    pct_multiracial = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Year: {}, Total: {}, Unsheltered: {}, Emergency shelter: {}, Transitional housing: {}".format(self.year, self.total, self.unsheltered, self.emergency_shelter, self.transitional_housing)

#data.seattle.gov API
class LowIncomeHousing(models.Model):
    number_of_units = models.IntegerField(null=False)
    year_placed_in_service = models.IntegerField(null=False)
    name = models.TextField(null=True)
    address = models.TextField(null=True)
    zip_code = models.TextField(null=True)
    council_district = models.IntegerField(null=True)
    hud = models.NullBooleanField(null=True)
    sha = models.NullBooleanField(null=True)
    state_or_county = models.NullBooleanField(null=True)
    wshfc = models.NullBooleanField(null=True)
    city_of_seattle = models.NullBooleanField(null=True)

    def __str__(self):
        return "Number of Units: {}, Year Placed In Service: {}, Name: {}, Address: {} {}, Council District: {}".format(self.number_of_units, self.year_placed_in_service, self.name, self.address, self.zip_code, self.council_district)

#data.seattle.gov API
class BuildingPermit(models.Model):
    permit_number = models.TextField(null=False)
    permit_class = models.TextField(null=False)
    permit_class_mapped = models.TextField(null=False)
    permit_type = models.TextField(null=True)
    permit_type_mapped = models.TextField(null=False)
    description = models.TextField(null=True)
    number_of_units = models.IntegerField(null=True)
    housing_units_removed = models.IntegerField(null=True)
    housing_units_added = models.IntegerField(null=True)
    permit_application_date = models.TextField(null=True)
    permit_approval_date = models.TextField(null=True)
    permit_completion_date = models.TextField(null=True)
    location = models.TextField(null=True)
    link = models.TextField(null=True)

    def __str__(self):
        return "Permit Number: {}, Permit Class: {} - {}, Permit Type: {} - {}, Description: {} , Number of Units: {}, # of Units Removed: {}, # of Units Added: {}".format(self.permit_number, self.permit_class, self.permit_class_mapped, self.permit_type, self.permit_type_mapped, self.description, self.number_of_units, self.housing_units_removed, self.housing_units_added)

# 2018 data only currently, from government watcher's spreadsheet
class EncampmentRemoval(models.Model):
    date = models.TextField(null=False)
    year = models.TextField(null=False)
    location = models.TextField(null=False)
    departments_responsible_for_removal = models.TextField(null=True)
    notes = models.TextField(null=True)
    found_on_city_property = models.NullBooleanField(null=True)
    vehicle_hazard = models.NullBooleanField(null=True)
    criminal_activity_beyond_drug_use = models.NullBooleanField(null=True)
    waste_and_debris = models.NullBooleanField(null=True)
    health_hazard_to_neighborhood = models.NullBooleanField(null=True)
    limited_emergency_services = models.NullBooleanField(null=True)
    scheduled_worksite = models.NullBooleanField(null=True)
    damage_to_environment = models.NullBooleanField(null=True)
    proximity_to_school_or_elderly = models.NullBooleanField(null=True)

    def __str__(self):
        return "Date of Removal: {}, {}, Location: {}, Departments responsible for removal: {}, Reasons for Removal: vehicle hazard - {}, criminal activity beyond drug use - {}, waste & debris - {}, health hazard to neighborhood - {}, limited emergency services - {}, scheduled worksite - {}, damage to environment - {}, proximity_to_school_or_elderly - {}".format(self.date, self.year, self.location, self.departments_responsible_for_removal, self.vehicle_hazard, self.criminal_activity, self.waste_and_debris, self.health_hazard_to_neighborhood, self.limited_emergency_services, self.scheduled_worksite, self.damage_to_environment, self.proximity_to_school_or_elderly)

# MFTE - Multi Family Tax Exempted Projects, developers receive tax exemption for setting aside portion of housing for low income. From data.seattle.gov API
class MFTEProject(models.Model):
    project_name = models.TextField(null=False)
    tax_exemption_start = models.IntegerField(null=True)
    tax_exemption_end = models.IntegerField(null=True)
    year_of_approval = models.IntegerField(null=True)
    address = models.TextField(null=False)
    council_district = models.IntegerField(null=True)
    targeted_area = models.TextField(null=True)
    subsidized = models.NullBooleanField(null=True)
    total_units = models.IntegerField(null=True)
    total_affordable_units = models.IntegerField(null=True)
    microhousing = models.NullBooleanField(null=True)
    # single efficiency dwelling unit (a form of microhousing)
    SEDU_total = models.IntegerField(null=True)
    SEDU_affordable = models.IntegerField(null=True)
    studio_units_total = models.IntegerField(null=True)
    studio_units_affordable = models.IntegerField(null=True)
    one_br_total = models.IntegerField(null=True)
    one_br_affordable = models.IntegerField(null=True)
    two_br_total = models.IntegerField(null=True)
    two_br_affordable = models.IntegerField(null=True)
    three_br_total = models.IntegerField(null=True)
    three_br_affordable = models.IntegerField(null=True)
    four_br_total = models.IntegerField(null=True)
    four_br_affordable = models.IntegerField(null=True)

    def __str__(self):
        return "Project Name: {}, Address: {}, Tax Exemption Start: {}, Tax Exemption End: {}, Total Units: {}, Total Affordable Units: {}".format(self.project_name, self.address, self.tax_exemption_start, self.tax_exemption_end, self.total_units, self.total_affordable_units)

#from US Census Bureau American Community Survey (ACS) 1year
class CommunitySurvey(models.Model):
    year = models.IntegerField(null=False)
    total_population = models.IntegerField(null=False)
    gini_index = models.FloatField(null=False)
    median_income = models.IntegerField(null=False)
    income_under_10000 = models.IntegerField(null=True)
    income_10000_14999 = models.IntegerField(null=True)
    income_15000_19999 = models.IntegerField(null=True)
    income_20000_24999 = models.IntegerField(null=True)
    income_25000_29999 = models.IntegerField(null=True)
    income_30000_34999 = models.IntegerField(null=True)
    income_35000_39999 = models.IntegerField(null=True)
    income_40000_44999 = models.IntegerField(null=True)
    income_45000_49999 = models.IntegerField(null=True)
    income_50000_59999 = models.IntegerField(null=True)
    income_60000_74999 = models.IntegerField(null=True)
    income_75000_99999 = models.IntegerField(null=True)
    income_100000_124999 = models.IntegerField(null=True)
    income_125000_149999 = models.IntegerField(null=True)
    income_150000_199999 = models.IntegerField(null=True)
    income_over_200000 = models.IntegerField(null=True)
    median_rent_studio = models.IntegerField(null=True)
    median_rent_1br = models.IntegerField(null=True)
    median_rent_2br = models.IntegerField(null=True)
    median_rent_3br = models.IntegerField(null=True)
    median_rent_4br = models.IntegerField(null=True)
    median_rent_5br = models.IntegerField(null=True)


    def __str__(self):
        return "Year: {}, Total Population: {}, Gini Index: {}, Median Income: {}, Median Rent for 1br: {}".format(self.year, self.total_population, self.gini_index, self.median_income, self.median_rent_1br)


#data.seattle.gov city budget API
class CityBudget(models.Model):
    fiscal_year = models.IntegerField(null=False)
    service = models.TextField(null=True)
    department = models.TextField(null=True)
    program = models.TextField(null=True)
    expense_category = models.TextField(null=True)
    expense_type = models.TextField(null=True)
    fund = models.TextField(null=True)
    fund_type = models.TextField(null=True)
    description = models.TextField(null=False)
    recommended_amount = models.TextField(null=True)
    approved_amount = models.TextField(null=False)

    def __str__(self):
        return "Fiscal Year: {}, Service: {}, Description: {}, Approved Amount: {}".format(self.fiscal_year, self.service, self.description, self.approved_amount)

#data from Redfin
class HousingMarket(models.Model):
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    homes_sold = models.IntegerField(null=True)
    inventory = models.IntegerField(null=True)
    number_of_new_listings = models.IntegerField(null=True)
    number_of_pending_sales = models.IntegerField(null=True)
    median_sale_price = models.TextField(null=True)
    pct_sold_above_list = models.TextField(null=True)
    avg_days_on_market = models.IntegerField(null=True)


    def __str__(self):
        return "Month/Year: {}/{}, Median Sale Price: {}, # of Homes Sold: {}, Avg # days on market: {}".format(self.month, self.year, self.median_sale_price, self.homes_sold, self.avg_days_on_market)
