# Generated by Django 2.0.2 on 2018-07-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='occupancy',
            field=models.IntegerField(default=1),
        ),
    ]
