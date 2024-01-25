# Generated by Django 5.0.1 on 2024-01-25 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_lounge_lounge_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lounge",
            name="local",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loungeLocal",
                to="restaurant.local",
                verbose_name="Local",
            ),
        ),
        migrations.AlterField(
            model_name="table",
            name="lounge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tableLounge",
                to="restaurant.lounge",
                verbose_name="Lounge",
            ),
        ),
    ]
