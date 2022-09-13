<<<<<<< HEAD
# Generated by Django 4.1 on 2022-09-13 10:44
=======
# Generated by Django 4.1 on 2022-09-13 13:49
>>>>>>> develop

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccumulationPoint",
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
                (
                    "materials",
                    models.ManyToManyField(
                        related_name="accumulation_points", to="materials.material"
                    ),
                ),
            ],
        ),
    ]
