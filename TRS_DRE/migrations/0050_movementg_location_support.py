# Generated by Django 4.2.14 on 2024-10-08 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0049_location_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementg',
            name='location_Support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.location_support'),
        ),
    ]
