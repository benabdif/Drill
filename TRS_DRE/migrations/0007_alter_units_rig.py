# Generated by Django 3.2.25 on 2024-06-23 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0006_movementg_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='units',
            name='rig',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='TRS_DRE.rigg'),
        ),
    ]
