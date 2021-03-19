from django.contrib import admin
from .models import EggplantDataSheet, EggplantDataSheetDescription

class EggplantDataSheetAdmin(admin.ModelAdmin):
    
    '''descriptor class for the EggplantDataSheet Administration'''

    list_display = [field.name for field in EggplantDataSheet._meta.get_fields()]


class EggplantDataSheetDescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'species',
        'location',
        'curator',
        'sowing_date',
        'planting_date',
    )

# Register your models here.
admin.site.register(EggplantDataSheetDescription, EggplantDataSheetDescriptionAdmin)
admin.site.register(EggplantDataSheet, EggplantDataSheetAdmin)
