# Generated by Django 2.2.2 on 2019-06-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_team_all_eyes_on_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='history',
            unique_together={('team', 'year')},
        ),
    ]
