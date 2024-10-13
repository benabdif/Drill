# Generated by Django 4.2.14 on 2024-10-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0043_repairsection_additional_repairsection_change_cellar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clean_Up_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clean_up_request_Number', models.IntegerField(blank=True, null=True)),
                ('clean_up_request_Date', models.DateField(blank=True, null=True)),
                ('clean_up_request_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_construction_contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_KPI', models.IntegerField(blank=True, null=True)),
                ('clean_up_start_Date', models.DateField(blank=True, null=True)),
                ('clean_Up_start_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_completion_date', models.DateField(blank=True, null=True)),
                ('clean_up_post_clean_Up_Turnover', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_monitored_by', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_Quantities_details', models.CharField(blank=True, max_length=200, null=True)),
                ('clean_up_project_team_details', models.CharField(blank=True, max_length=200, null=True)),
                ('clean_up_pre_Clean_Up_Turnover', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_Criticality', models.CharField(choices=[('YES', 'NO')], default='N/A', max_length=10)),
            ],
        ),
    ]
