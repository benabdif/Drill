# Generated by Django 4.2.14 on 2024-09-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0026_remove_rigg_contractor_remove_rigg_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='construction_departmeent',
            name='Construction_Status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
