from django.contrib import admin

from .models import HomelessCount, LowIncomeHousing, BuildingPermit

admin.site.register(HomelessCount)
admin.site.register(LowIncomeHousing)
admin.site.register(BuildingPermit)
