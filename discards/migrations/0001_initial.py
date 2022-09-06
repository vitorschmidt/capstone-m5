# Generated by Django 4.1 on 2022-09-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discard",
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
                ("address", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=50)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "companies",
                    models.ManyToManyField(
                        related_name="discards", to="companies.company"
                    ),
                ),
            ],
        ),
    ]
