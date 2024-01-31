# Generated by Django 5.0.1 on 2024-01-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(auto_now_add=True, null=True, verbose_name="Fecha"),
        ),
        migrations.AddField(
            model_name="order",
            name="time",
            field=models.TimeField(auto_now_add=True, null=True, verbose_name="Hora"),
        ),
    ]
