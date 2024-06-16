# Generated by Django 3.2.25 on 2024-05-20 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rigg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wellg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movementg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.rigg')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.wellg')),
            ],
        ),
    ]
