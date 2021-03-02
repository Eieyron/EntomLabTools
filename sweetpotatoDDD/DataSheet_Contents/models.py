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
    curator = models.CharField(max_length=255)

    # Plant Characteristics
    plant_growth_habit  = models.IntegerField() #3579
    ground_cover        = models.IntegerField() #3579

    # Vine Characteristics
    twining                 = models.IntegerField() #03579
    predominant_vine_color  = models.IntegerField() #1-9
    secondary_vine_color    = models.IntegerField() #0-7
    vine_tip_pubescence     = models.IntegerField() #0357
    vine_internode_length   = models.IntegerField() #13579
    vine_internode_diameter = models.IntegerField() #13579

    # Mature Leaf Shape
    general_outline_of_the_leaf = models.IntegerField() #1-7
    leaf_lobes_type             = models.IntegerField() #013579
    leaf_lobe_number            = models.IntegerField() #013579
    shape_of_central_leaf_lobes = models.IntegerField() #0-7
    abaxial_leaf_vein_pigmentation  = models.IntegerField() #1-9
    mature_leaf_size            = models.IntegerField() #3579

    # Foliage Color
    mature_leaf_color   = models.IntegerField() #1-9
    immature_leaf_color = models.IntegerField() #1-9
    petiole_pigmentation    = models.IntegerField() #1-9
    petiole_length          = models.IntegerField() #1-9

    # Storage Root
    storage_root_outline_shown_in_longitudinal_section = models.IntegerField() #1-9
    storage_root_surface_defects    = models.IntegerField() #0-7,9
    storage_root_cortex_thickness   = models.IntegerField() #13579
    predominant_skin_color          = models.IntegerField() #1-9
    intensity_of_predominant_skin_color = models.IntegerField() #1-3
    secondary_skin_color            = models.IntegerField() #1-9
    predominant_flesh_color         = models.IntegerField() #1-9
    secondary_flesh_color           = models.IntegerField() #0-9
    distribution_of_secondary_flesh_color   = models.IntegerField() #0-9
    
    


