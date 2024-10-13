# Generated by Django 3.2.25 on 2024-06-24 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0010_auto_20240623_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('contractor_ID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('contractor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rigg',
            name='Contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.contractor'),
        ),
    ]