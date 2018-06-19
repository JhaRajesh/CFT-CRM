# Generated by Django 2.0.6 on 2018-06-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time_in', models.DateTimeField(null=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Pending', 'Pending')], default='Pending', max_length=7)),
                ('leave_type', models.CharField(choices=[('PL', 'Privilege leave'), ('CL', 'Casual leave'), ('Half Day', 'Half Day')], max_length=8, null=True)),
                ('note', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
