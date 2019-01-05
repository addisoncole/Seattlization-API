from django.db import models

#year="", total="", unsheltered="", emergency_shelter="", transitional_housing=""

class HomelessCount(models.Model):
    year = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    unsheltered = models.IntegerField(null=True)
    emergency_shelter = models.IntegerField(null=True)
    transitional_housing = models.IntegerField(null=True)

    def __str__(self):
        return "Year:{}, Total:{}, {} {}".format(self.year, self.total, self.unsheltered, self.emergency_shelter, self.transitional_housing)
