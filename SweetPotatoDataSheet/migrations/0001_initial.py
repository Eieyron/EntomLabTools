# Generated by Django 3.1.7 on 2021-03-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SweetPotatoDataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('planting_date', models.DateField()),
                ('sowing_date', models.DateField()),
                ('accession_no', models.CharField(max_length=50)),
                ('plot_no', models.IntegerField()),
                ('curator', models.CharField(max_length=255)),
                ('plant_growth_habit', models.IntegerField()),
                ('ground_cover', models.IntegerField()),
                ('twining', models.IntegerField()),
                ('predominant_vine_color', models.IntegerField()),
                ('secondary_vine_color', models.IntegerField()),
                ('vine_tip_pubescence', models.IntegerField()),
                ('vine_internode_length', models.IntegerField()),
                ('vine_internode_diameter', models.IntegerField()),
                ('general_outline_of_the_leaf', models.IntegerField()),
                ('leaf_lobes_type', models.IntegerField()),
                ('leaf_lobe_number', models.IntegerField()),
                ('shape_of_central_leaf_lobes', models.IntegerField()),
                ('abaxial_leaf_vein_pigmentation', models.IntegerField()),
                ('mature_leaf_size', models.IntegerField()),
                ('mature_leaf_color', models.IntegerField()),
                ('immature_leaf_color', models.IntegerField()),
                ('petiole_pigmentation', models.IntegerField()),
                ('petiole_length', models.IntegerField()),
                ('storage_root_outline_shown_in_longitudinal_section', models.IntegerField()),
                ('storage_root_surface_defects', models.IntegerField()),
                ('storage_root_cortex_thickness', models.IntegerField()),
                ('predominant_skin_color', models.IntegerField()),
                ('intensity_of_predominant_skin_color', models.IntegerField()),
                ('secondary_skin_color', models.IntegerField()),
                ('predominant_flesh_color', models.IntegerField()),
                ('secondary_flesh_color', models.IntegerField()),
                ('distribution_of_secondary_flesh_color', models.IntegerField()),
            ],
        ),
    ]