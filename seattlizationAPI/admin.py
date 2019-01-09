from django.contrib import admin

from .models import HomelessCount, LowIncomeHousing, BuildingPermit, EncampmentRemoval

admin.site.register(HomelessCount)
admin.site.register(LowIncomeHousing)
admin.site.register(BuildingPermit)
admin.site.register(EncampmentRemoval)
