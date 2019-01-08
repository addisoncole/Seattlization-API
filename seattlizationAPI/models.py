from django.db import models

class HomelessCount(models.Model):
    year = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    unsheltered = models.IntegerField(null=True)
    emergency_shelter = models.IntegerField(null=True)
    transitional_housing = models.IntegerField(null=True)
    number_in_seattle = models.IntegerField(null=True)
    pct_female = models.IntegerField(null=True)
    pct_male = models.IntegerField(null=True)
    pct_trans = models.IntegerField(null=True)
    pct_gnc = models.IntegerField(null=True)
    pct_white = models.IntegerField(null=True)
    pct_black = models.IntegerField(null=True)
    pct_latino = models.IntegerField(null=True)
    pct_indigenous = models.IntegerField(null=True)
    pct_asian = models.IntegerField(null=True)
    pct_hawaiian_api = models.IntegerField(null=True)
    pct_multiracial = models.IntegerField(null=True)

    def __str__(self):
        return "Year: {}, Total: {}, Unsheltered: {}, Emergency shelter: {}, Transitional housing: {}".format(self.year, self.total, self.unsheltered, self.emergency_shelter, self.transitional_housing)

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
        return "Permit Number: {}, Permit Class: {} - {}, Permit Type: {} - {}, Description: {} , Number of Units: {}, # of Units Removed: {}, # of Units Added: ".format(self.permit_number, self.permit_class, self.permit_class_mapped, self.permit_type, self.permit_type_mapped, self.description, self.number_of_units, self.housing_units_removed, self.housing_units_added)
