# Generated by Django 2.0.2 on 2018-07-07 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_types', '0003_auto_20180707_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='bed',
        ),
        migrations.AddField(
            model_name='roomtype',
            name='bed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='room_types.Bed'),
            preserve_default=False,
        ),
    ]
