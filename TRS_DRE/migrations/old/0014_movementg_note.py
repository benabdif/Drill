# Generated by Django 4.2.9 on 2024-08-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TRS_DRE", "0013_auto_20240624_1407"),
    ]

    operations = [
        migrations.AddField(
            model_name="movementg",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]
