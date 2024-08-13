# Generated by Django 4.2.9 on 2024-08-11 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("ToDoList", "0009_alter_groupworkshop_members_delete_employee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="assigned_to",
        ),
        migrations.AddField(
            model_name="task",
            name="content_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="object_id",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]