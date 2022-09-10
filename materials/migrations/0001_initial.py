# Generated by Django 4.1.1 on 2022-09-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('dangerousness', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('Reciclavel', 'Reciclavel'), ('Não Reciclavel', 'Naoreciclavel'), ('Hospitalar', 'Hospitalar'), ('Orgânico', 'Organico'), ('Eletrônico', 'Eletronico'), ('Agricola', 'Agricola'), ('Radioativo', 'Radiotivo'), ('Industrial', 'Industrial')], default='Reciclavel', max_length=40)),
                ('infos', models.CharField(max_length=500)),
                ('decomposition', models.PositiveIntegerField()),
            ],
        ),
    ]
