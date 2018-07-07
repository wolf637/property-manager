# Generated by Django 2.0.2 on 2018-07-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_room_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='checked_in',
        ),
        migrations.RemoveField(
            model_name='room',
            name='checked_out',
        ),
        migrations.AddField(
            model_name='room',
            name='empty',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='room',
            name='ready',
            field=models.BooleanField(default=True),
        ),
    ]