# Generated by Django 3.2.25 on 2024-06-24 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0012_auto_20240624_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='update_L',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movementg',
            name='Contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.contractor'),
        ),
        migrations.AddField(
            model_name='movementg',
            name='Eng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.engineering'),
        ),
    ]