# Generated by Django 4.2.14 on 2024-10-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0048_movementg_clean_up_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='location_Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_location_support_Request_Number', models.IntegerField(blank=True, null=True)),
                ('on_location_support_Request_date', models.DateField(blank=True, null=True)),
                ('on_location_support_Request_status', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_dispatch_By', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_Remark', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
