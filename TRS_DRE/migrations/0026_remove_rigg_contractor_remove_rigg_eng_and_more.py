# Generated by Django 4.2.9 on 2024-09-24 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("TRS_DRE", "0025_rename_engineering_name_rigg_current_assigned_unit_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rigg",
            name="Contractor",
        ),
        migrations.RemoveField(
            model_name="rigg",
            name="Eng",
        ),
        migrations.RemoveField(
            model_name="rigg",
            name="Units",
        ),
    ]