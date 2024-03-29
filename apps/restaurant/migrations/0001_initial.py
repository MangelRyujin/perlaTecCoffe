# Generated by Django 5.0.1 on 2024-01-25 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Local",
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
                    "local_name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Local name"
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Local",
                "verbose_name_plural": "Locals",
            },
        ),
        migrations.CreateModel(
            name="Lounge",
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
                    "lounge_name",
                    models.CharField(max_length=255, verbose_name="Lounge name"),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "local",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loungeLocal",
                        to="restaurant.local",
                        verbose_name="Local",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lounge",
                "verbose_name_plural": "Lounge",
            },
        ),
        migrations.CreateModel(
            name="Table",
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
                    "state",
                    models.CharField(
                        choices=[("busy", "busy"), ("available", "available")],
                        default="available",
                        max_length=10,
                        verbose_name="Table state",
                    ),
                ),
                ("number", models.PositiveIntegerField(verbose_name="Table number")),
                ("active", models.BooleanField(default=True)),
                (
                    "max_people",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Maximum number of people"
                    ),
                ),
                (
                    "lounge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tableLounge",
                        to="restaurant.lounge",
                        verbose_name="Lounge",
                    ),
                ),
            ],
            options={
                "verbose_name": "Table",
                "verbose_name_plural": "Tables",
            },
        ),
    ]
