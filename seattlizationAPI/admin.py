from django.contrib import admin

from .models import HomelessCount, LowIncomeHousing

admin.site.register(HomelessCount)
admin.site.register(LowIncomeHousing)
