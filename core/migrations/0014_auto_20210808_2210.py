# Generated by Django 3.1 on 2021-08-08 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_playerstats_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetplayer',
            options={'ordering': ['rank']},
        ),
    ]
