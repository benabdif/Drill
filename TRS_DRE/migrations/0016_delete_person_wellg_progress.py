# Generated by Django 4.2.9 on 2024-08-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TRS_DRE", "0015_wellg_location"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Person",
        ),
        migrations.AddField(
            model_name="wellg",
            name="progress",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
