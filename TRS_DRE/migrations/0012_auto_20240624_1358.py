# Generated by Django 3.2.25 on 2024-06-24 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0011_auto_20240624_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineering',
            fields=[
                ('Eng_ID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('Eng_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rigg',
            name='Eng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.engineering'),
        ),
    ]
