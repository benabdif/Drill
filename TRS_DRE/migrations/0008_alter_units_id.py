# Generated by Django 3.2.25 on 2024-06-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0007_alter_units_rig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='units',
            name='ID',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]