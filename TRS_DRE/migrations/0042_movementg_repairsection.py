# Generated by Django 4.2.14 on 2024-10-07 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0041_remove_repairsection_repair_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementg',
            name='RepairSection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.repairsection'),
        ),
    ]
