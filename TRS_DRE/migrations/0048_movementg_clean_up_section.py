# Generated by Django 4.2.14 on 2024-10-08 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRS_DRE', '0047_alter_clean_up_section_clean_up_criticality'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementg',
            name='Clean_Up_Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.clean_up_section'),
        ),
    ]
