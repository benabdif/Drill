# Generated by Django 4.2.14 on 2024-10-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0038_movementg_rig_move'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairsection',
            name='sand_removal',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
