# Generated by Django 4.2.14 on 2024-10-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0042_movementg_repairsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairsection',
            name='Additional',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Change_Cellar',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Complete_Repair',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Extension',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Modification',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Re_Compaction',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
