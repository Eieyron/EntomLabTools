from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# STC - subject to change

class SweetPotato_Data(models.Model):

    species = models.CharField(max_length=50)
    location = models.CharField(max_length=50) # STC
    planting_date = models.DateField(auto_now=False, auto_now_add=False)
    sowing_date = models.DateField(auto_now=False, auto_now_add=False)
    accession_no = models.CharField(max_length=50)
    plot_no = models.IntegerField()
    curator = models.CharField(max_length=50)

    # Plant Characteristics
    plant_growth_habit  = models.IntegerField() #3579
    ground_cover        = models.IntegerField() #3579

    # Vine Characteristics
    twining                 = models.IntegerField() #03579
    predominant_vine_color  = models.IntegerField() #1-9
