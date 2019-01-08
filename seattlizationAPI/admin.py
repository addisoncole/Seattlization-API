from django.contrib import admin

# Register your models here.
from .models import HomelessCount, LowIncomeHousing

admin.site.register(HomelessCount)
admin.site.register(LowIncomeHousing)
