# Generated by Django 4.2.9 on 2024-07-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eHighlight", "0008_remove_ehighlight_record_highlight_c_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ehighlight_record",
            name="details",
            field=models.TextField(blank=True, null=True),
        ),
    ]
