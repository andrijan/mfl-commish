# Generated by Django 3.1 on 2020-08-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190626_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('year',)},
        ),
        migrations.AlterModelOptions(
            name='rookieplayer',
            options={'ordering': ('pick',)},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('-prediction_record',)},
        ),
        migrations.AddField(
            model_name='team',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
