# Generated by Django 4.0.3 on 2023-03-14 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0016_auto_20190401_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='rollNumber',
        ),
    ]
