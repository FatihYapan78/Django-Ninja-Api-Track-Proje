# Generated by Django 5.0 on 2023-12-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("track", "0002_alter_track_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="last_play",
            field=models.DateField(),
        ),
    ]
