# Generated by Django 3.2.25 on 2024-06-23 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0004_movementg_is_cleaned_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name_unit', models.CharField(max_length=100)),
                ('Unit_supervision', models.CharField(max_length=100)),
                ('rig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='TRS_DRE.rigg')),
            ],
        ),
    ]
