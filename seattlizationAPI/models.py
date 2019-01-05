from django.db import models

#year="", total="", unsheltered="", emergency_shelter="", transitional_housing=""

class HomelessCount(models.Model):
    year = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    unsheltered = models.IntegerField()
    emergency_shelter = models.IntegerField()
    transitional_housing = models.IntegerField()

    def __str__(self):
        return "Year:{}, Total:{}, {}".format(self.year, self.total, self.unsheltered)
