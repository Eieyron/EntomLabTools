from django.contrib import admin
from .models import SweetPotatoDataSheet, SweetPotatoDataSheetDescription

admin.site.site_header = 'Entomology Database'

# @admin.register
class SweetPotatoDataSheetAdmin(admin.ModelAdmin):
    
    '''descriptor class for the SweetPotatoDataSheet Administration'''

    list_display = [field.name for field in SweetPotatoDataSheet._meta.get_fields()]

class SweetPotatoDataSheetDescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'species',
        'location',
        'curator',
        'sowing_date',
        'planting_date',
    )

# Register your models here.
admin.site.register(SweetPotatoDataSheetDescription, SweetPotatoDataSheetDescriptionAdmin)
admin.site.register(SweetPotatoDataSheet, SweetPotatoDataSheetAdmin)
