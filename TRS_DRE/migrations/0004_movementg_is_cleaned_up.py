# Generated by Django 4.2.13 on 2024-06-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TRS_DRE", "0003_auto_20240615_1451"),
    ]

    operations = [
        migrations.AddField(
            model_name="movementg",
            name="is_cleaned_up",
            field=models.BooleanField(default=False),
        ),
    ]