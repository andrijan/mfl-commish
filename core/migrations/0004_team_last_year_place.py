# Generated by Django 2.2.2 on 2019-06-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190612_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='last_year_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
