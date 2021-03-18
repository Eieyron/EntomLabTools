from django.contrib import admin
from .models import EggplantDataSheet

class EggplantDataSheetAdmin(admin.ModelAdmin):
    
    '''descriptor class for the EggplantDataSheet Administration'''

    list_filter = (
        'rep_no',
        'plot_no',
        'plant_no',
        'plant_breadth',
        'petiole_length',
        'leaf_blade_length',
        'leaf_blade_width',
    )


# Register your models here.
admin.site.register(EggplantDataSheet, EggplantDataSheetAdmin)
