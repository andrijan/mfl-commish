from django.contrib import admin

from . import models


@admin.register(models.Player)
class Player(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'team', 'last_year_team']
    list_filter = ['team']


class PlayerInline(admin.StackedInline):
    model = models.Player
    fk_name = 'team'


class AssetPlayer(admin.TabularInline):
    max_num = 5
    model = models.AssetPlayer
    autocomplete_fields = ['player']


class AddKeyPlayer(admin.TabularInline):
    model = models.AddKeyPlayer
    autocomplete_fields = ['player']


class SubKeyPlayer(admin.TabularInline):
    model = models.SubKeyPlayer
    autocomplete_fields = ['player']


class RookiePlayer(admin.TabularInline):
    model = models.RookiePlayer
    autocomplete_fields = ['player']


class History(admin.TabularInline):
    model = models.History


@admin.register(models.Team)
class Team(admin.ModelAdmin):
    list_filter = ['year']
    list_display = [
        'name',
        'year',
        'mfl_id',
        'is_active',
        'prediction_place',
        'quarterbacks_rating',
        'running_backs_rating',
        'receivers_rating',
    ]
    autocomplete_fields = [
        'all_eyes_on_player',
        'x_factor_player',
    ]

    inlines = [
        AssetPlayer,
        AddKeyPlayer,
        SubKeyPlayer,
        RookiePlayer,
        History,
    ]
