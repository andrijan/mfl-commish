# Generated by Django 2.2.1 on 2019-06-01 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddKeyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AssetPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('D', 'Defence'), ('QB', 'Quarterback'), ('RB', 'Running Back'), ('WR', 'Wide Receiver'), ('TE', 'Tight End')], max_length=255)),
                ('acquired', models.CharField(blank=True, max_length=255, null=True)),
                ('is_rookie', models.BooleanField()),
                ('auction_price', models.CharField(blank=True, max_length=255, null=True)),
                ('rookie_pick', models.CharField(blank=True, max_length=255, null=True)),
                ('waiver_price', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RookiePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(max_length=255)),
                ('fp_rank', models.CharField(blank=True, max_length=255, null=True)),
                ('stars', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rookie_rookie_team', to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='SubKeyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_key_players', to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('mfl_id', models.CharField(blank=True, max_length=255, null=True)),
                ('base_color', models.CharField(blank=True, max_length=255, null=True)),
                ('secondary_color', models.CharField(blank=True, max_length=255, null=True)),
                ('is_dark', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('quarterbacks', models.TextField()),
                ('running_backs', models.TextField()),
                ('receivers', models.TextField()),
                ('all_eyes_on', models.TextField()),
                ('x_factor', models.TextField()),
                ('x_factor_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('key_to_championship_title', models.CharField(blank=True, max_length=255)),
                ('key_to_championship', models.TextField()),
                ('prediction_place', models.CharField(blank=True, max_length=255, null=True)),
                ('prediction_record', models.CharField(blank=True, max_length=255, null=True)),
                ('last_year_record', models.CharField(blank=True, max_length=255, null=True)),
                ('last_year_ppg', models.CharField(blank=True, max_length=255, null=True)),
                ('last_year_papg', models.CharField(blank=True, max_length=255, null=True)),
                ('scouting_report', models.TextField()),
                ('scouting_report_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('all_eyes_on_player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='all_eyes_on_team', to='core.Player')),
                ('key_adds', models.ManyToManyField(related_name='key_adds', through='core.AddKeyPlayer', to='core.Player')),
                ('key_subs', models.ManyToManyField(related_name='key_subs', through='core.SubKeyPlayer', to='core.Player')),
                ('rookies', models.ManyToManyField(related_name='rookie_team', through='core.RookiePlayer', to='core.Player')),
                ('top_assets', models.ManyToManyField(related_name='assets', through='core.AssetPlayer', to='core.Player')),
                ('x_factor_player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='x_factor_team', to='core.Player')),
            ],
        ),
        migrations.AddField(
            model_name='subkeyplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_key_players', to='core.Team'),
        ),
        migrations.AddField(
            model_name='rookieplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rookie_rookie_player', to='core.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='last_year_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='core.Team'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('playoff_wins', models.IntegerField(default=0)),
                ('playoff_losses', models.IntegerField(default=0)),
                ('playoff_appearence', models.BooleanField(default=False)),
                ('championship', models.BooleanField(default=False)),
                ('runner_up', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='core.Team')),
            ],
        ),
        migrations.AddField(
            model_name='assetplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_players', to='core.Player'),
        ),
        migrations.AddField(
            model_name='assetplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_players', to='core.Team'),
        ),
        migrations.AddField(
            model_name='addkeyplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_key_players', to='core.Player'),
        ),
        migrations.AddField(
            model_name='addkeyplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_key_players', to='core.Team'),
        ),
    ]
