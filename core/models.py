from django.db import models


class Team(models.Model):
    year = models.IntegerField(default=2019)
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    mfl_id = models.CharField(max_length=255, blank=True, null=True)
    base_color = models.CharField(max_length=255, blank=True, null=True)
    secondary_color = models.CharField(max_length=255, blank=True, null=True)
    is_dark = models.BooleanField(default=True)
    description = models.TextField()
    quarterbacks = models.TextField()
    quarterback_image = models.ImageField(blank=True, null=True)
    quarterbacks_rating = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    running_backs = models.TextField()
    running_back_image = models.ImageField(blank=True, null=True)
    running_backs_rating = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    receivers = models.TextField()
    receiver_image = models.ImageField(blank=True, null=True)
    receivers_rating = models.CharField(max_length=255, blank=True, null=True)

    all_eyes_on_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='all_eyes_on_team',
    )
    all_eyes_on = models.TextField()
    all_eyes_on_image = models.ImageField(blank=True, null=True)

    x_factor_player = models.ForeignKey(
        'Player',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='x_factor_team'
    )
    x_factor = models.TextField()
    x_factor_image = models.ImageField(blank=True, null=True)

    key_to_championship_title = models.CharField(max_length=255, blank=True)
    key_to_championship = models.TextField()

    rookies = models.ManyToManyField(
        'Player',
        through='RookiePlayer',
        related_name='rookie_team'
    )

    prediction_place = models.CharField(max_length=255, null=True, blank=True)
    prediction_place_suffix = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    prediction_record = models.CharField(max_length=255, null=True, blank=True)

    last_year_record = models.CharField(max_length=255, null=True, blank=True)
    last_year_ppg = models.CharField(max_length=255, null=True, blank=True)
    last_year_papg = models.CharField(max_length=255, null=True, blank=True)
    last_year_place = models.CharField(max_length=255, null=True, blank=True)

    top_assets = models.ManyToManyField(
        'Player',
        through='AssetPlayer',
        related_name='assets'
    )
    key_adds = models.ManyToManyField(
        'Player',
        through='AddKeyPlayer',
        related_name='key_adds'
    )
    key_subs = models.ManyToManyField(
        'Player',
        through='SubKeyPlayer',
        related_name='key_subs'
    )

    scouting_report = models.TextField()
    scouting_report_image = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-prediction_record', )

    def __str__(self):
        return '{}: {}'.format(self.year, self.name)


class AssetPlayer(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='asset_players'
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='asset_players'
    )
    rank = models.IntegerField()

    def __str__(self):
        return self.player.name


class AddKeyPlayer(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='add_key_players'
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='add_key_players'
    )
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.player.name


class SubKeyPlayer(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='sub_key_players'
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='sub_key_players'
    )
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.player.name


class History(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='history'
    )
    year = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    playoff_wins = models.IntegerField(default=0)
    playoff_losses = models.IntegerField(default=0)
    playoff_appearence = models.BooleanField(default=False)
    championship = models.BooleanField(default=False)
    runner_up = models.BooleanField(default=False)

    class Meta:
        unique_together = ('team', 'year')
        ordering = ('year', )

    def __str__(self):
        return self.team.name


class RookiePlayer(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='rookie_rookie_player'
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='rookie_rookie_team'
    )
    pick = models.CharField(max_length=255)
    fp_rank = models.CharField(max_length=255, blank=True, null=True)
    stars = models.IntegerField(default=0)

    class Meta:
        ordering = ('pick', )

    def __str__(self):
        return self.player.name


class Player(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='players'
    )
    name = models.CharField(max_length=255)
    mfl_id = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, choices=[
        ('D', 'Defence'),
        ('QB', 'Quarterback'),
        ('RB', 'Running Back'),
        ('WR', 'Wide Receiver'),
        ('TE', 'Tight End'),
    ])
    acquired = models.CharField(max_length=255, blank=True, null=True)
    last_year_team = models.ForeignKey(
        Team,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    is_rookie = models.BooleanField(default=False)
    adp = models.CharField(max_length=255, blank=True, null=True)
    auction_price = models.CharField(max_length=255, blank=True, null=True)
    rookie_pick = models.CharField(max_length=255, blank=True, null=True)
    waiver_price = models.CharField(max_length=255, blank=True, null=True)

    @property
    def stats_2020(self):
        try:
            return self.stats.get(year=2020)
        except PlayerStats.DoesNotExist:
            return {}

    def __str__(self):
        return self.name

class PlayerStats(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    year = models.IntegerField()
    points = models.FloatField()
    games_played = models.IntegerField()
    rushing_yards = models.IntegerField()
    rushing_tds = models.IntegerField()
    receptions = models.IntegerField(default=0)
    receiving_yards = models.IntegerField()
    receiving_tds = models.IntegerField()
    passing_yards = models.IntegerField()
    passing_tds = models.IntegerField()
