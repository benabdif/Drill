# Generated by Django 4.2.14 on 2024-09-30 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0031_rename_construction_departmeents_movementg_construction_departmeent'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementg',
            name='Cellar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.cellar'),
        ),
    ]
