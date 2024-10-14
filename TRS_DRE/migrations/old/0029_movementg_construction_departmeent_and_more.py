# Generated by Django 4.2.14 on 2024-09-29 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0028_alter_movementg_contractor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementg',
            name='Construction_Departmeent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.construction_departmeent'),
        ),
        migrations.AlterField(
            model_name='movementg',
            name='Contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.contractor'),
        ),
    ]