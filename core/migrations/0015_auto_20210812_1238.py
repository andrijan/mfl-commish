# Generated by Django 3.1 on 2021-08-12 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210808_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='mfl_id',
            new_name='sleeper_id',
        ),
    ]
