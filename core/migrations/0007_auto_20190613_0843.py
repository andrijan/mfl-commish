# Generated by Django 2.2.2 on 2019-06-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_team_prediction_place_suffix'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='adp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='mfl_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='is_rookie',
            field=models.BooleanField(default=False),
        ),
    ]
