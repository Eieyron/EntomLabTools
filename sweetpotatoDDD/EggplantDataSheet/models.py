from django.db import models

# Create your models here.

class EggplantDataSheet(models.Model):

    rep_no      = models.IntegerField()
    plot_no     = models.IntegerField()
    plant_no    = models.IntegerField()
    plant_height_at_flowering_stage = models.FloatField() # cm
    plant_breadth       = models.FloatField() # cm
    petiole_length      = models.FloatField() # cm
    leaf_blade_length   = models.FloatField() # cm
    leaf_blade_width    = models.FloatField() # cm
    leaf_blade_tip_angle    = models.IntegerField() 
    plant_growth_habit  = models.IntegerField()
    plant_branching     = models.IntegerField()
    stem_anthocyanin_coloration = models.IntegerField()
    stem_intensity_of_anthocyanin_coloration = models.IntegerField()
    stem_pubescence     = models.IntegerField()
    petiole_color       = models.IntegerField()
    leaf_blade_lobing   = models.IntegerField()
    leaf_blade_color    = models.IntegerField()
    leaf_blade_intensity_of_green_color = models.IntegerField()
    leaf_blade_blistering   = models.IntegerField()
    leaf_prickles   = models.IntegerField()
    leaf_hairs  = models.IntegerField()

    def __str__(self):
        return 'Eggplant | Rep:{} | Plot:{} | Plant:{} '.format(self.rep_no, self.plot_no, self.plant_no)
