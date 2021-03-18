# Generated by Django 3.1.7 on 2021-03-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EggplantDataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_no', models.IntegerField()),
                ('plot_no', models.IntegerField()),
                ('plant_no', models.IntegerField()),
                ('plant_height_at_flowering_stage', models.FloatField()),
                ('plant_breadth', models.FloatField()),
                ('petiole_length', models.FloatField()),
                ('leaf_blade_length', models.FloatField()),
                ('leaf_blade_width', models.FloatField()),
                ('leaf_blade_tip_angle', models.IntegerField()),
                ('plant_growth_habit', models.IntegerField()),
                ('plant_branching', models.IntegerField()),
                ('stem_anthocyanin_coloration', models.IntegerField()),
                ('stem_intensity_of_anthocyanin_coloration', models.IntegerField()),
                ('stem_pubescence', models.IntegerField()),
                ('petiole_color', models.IntegerField()),
                ('leaf_blade_lobing', models.IntegerField()),
                ('leaf_blade_color', models.IntegerField()),
                ('leaf_blade_intensity_of_green_color', models.IntegerField()),
                ('leaf_blade_blistering', models.IntegerField()),
                ('leaf_prickles', models.IntegerField()),
                ('leaf_hairs', models.IntegerField()),
            ],
        ),
    ]