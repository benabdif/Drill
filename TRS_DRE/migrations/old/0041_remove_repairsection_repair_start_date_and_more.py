# Generated by Django 4.2.14 on 2024-10-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0040_alter_repairsection_sand_removal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairsection',
            name='Repair_Start_date',
        ),
        migrations.AlterField(
            model_name='repairsection',
            name='Contractor_Contractor_Repair',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='repairsection',
            name='Repair_Start_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]