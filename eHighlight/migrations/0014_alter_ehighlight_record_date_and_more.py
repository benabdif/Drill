# Generated by Django 4.2.9 on 2024-07-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eHighlight", "0013_alter_ehighlight_record_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ehighlight_record",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ehighlight_record",
            name="user_date",
            field=models.DateField(auto_now_add=True, default="2024-07-18"),
            preserve_default=False,
        ),
    ]
