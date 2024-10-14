# Generated by Django 4.2.9 on 2024-10-13 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee_2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WellSiteConstruction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "managers",
                    models.ManyToManyField(
                        related_name="construction_sites", to="ToDoList.manager"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "assigned_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supervisor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supervisors",
                        to="ToDoList.manager",
                    ),
                ),
                (
                    "construction_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supervisors",
                        to="ToDoList.wellsiteconstruction",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GroupWorkshop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("members", models.ManyToManyField(to="ToDoList.employee_2")),
                ("tasks", models.ManyToManyField(to="ToDoList.task")),
            ],
        ),
        migrations.AddField(
            model_name="employee_2",
            name="supervisor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employees",
                to="ToDoList.supervisor",
            ),
        ),
        migrations.AddField(
            model_name="employee_2",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
