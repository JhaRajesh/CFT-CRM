# Generated by Django 2.0.6 on 2018-06-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl', models.IntegerField(default=8)),
                ('cl', models.IntegerField(default=8)),
                ('half_day', models.IntegerField(default=8)),
                ('comp_off', models.IntegerField(default=8)),
            ],
        ),
    ]
