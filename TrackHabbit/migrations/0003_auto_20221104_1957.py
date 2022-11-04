# Generated by Django 3.2.16 on 2022-11-04 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TrackHabbit', '0002_dailyrecord_habit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyrecord',
            old_name='habit',
            new_name='habit_key',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]