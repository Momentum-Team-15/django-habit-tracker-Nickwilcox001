# Generated by Django 3.2.16 on 2022-11-06 22:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TrackHabbit', '0004_rename_date_dailyrecord_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyrecord',
            name='created_at',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
