from django.db import models

#year="", total="", unsheltered="", emergency_shelter="", transitional_housing=""

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
