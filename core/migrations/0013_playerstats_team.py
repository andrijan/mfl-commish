# Generated by Django 3.1 on 2021-08-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_playerstats_receptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstats',
            name='team',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
