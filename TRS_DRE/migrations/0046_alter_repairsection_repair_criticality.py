# Generated by Django 4.2.14 on 2024-10-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0045_alter_repairsection_repair_criticality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairsection',
            name='Repair_Criticality',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='N/A', max_length=10),
        ),
    ]