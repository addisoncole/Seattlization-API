from django.contrib import admin

from .models import HomelessCount, LowIncomeHousing, BuildingPermit, EncampmentRemoval, MFTEProject, CommunitySurvey, CityBudget

admin.site.register(HomelessCount)
admin.site.register(LowIncomeHousing)
admin.site.register(BuildingPermit)
admin.site.register(EncampmentRemoval)
admin.site.register(MFTEProject)
admin.site.register(CommunitySurvey)
admin.site.register(CityBudget)
