# Generated by Django 4.1.1 on 2022-09-12 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleCollect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('scheduling', models.DateTimeField()),
                ('city', models.CharField(max_length=120)),
                ('materials', models.ManyToManyField(related_name='schedule_collects', to='materials.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_collect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
