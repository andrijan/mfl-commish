import requests
import lxml.html

from . import models


BASE_URL = 'https://www74.myfantasyleague.com/2019/export'


def import_teams():
    base = 'https://www74.myfantasyleague.com/'
    years = [2016, 2017, 2018]
    for year in years:
        url = '{}{}/export?TYPE=leagueStandings&L=76173&APIKEY=&JSON=1'.format(
            base,
            str(year)
        )
        res = requests.get(url).json()
        franchises = res['leagueStandings']['franchise']
        for franchise in franchises:
            team, _ = models.Team.objects.get_or_create(
                mfl_id=franchise['id'],
            )
            if year == 2018:
                team.last_year_record = (
                    franchise['h2hw'] + '-' + franchise['h2hl']
                )
                team.last_year_ppg = float(franchise['pf']) / 13.0
                team.last_year_papg = float(franchise['pa']) / 13.0
                team.save()
            models.History.objects.get_or_create(
                team=team,
                year=year,
                defaults={
                    'wins': franchise['h2hw'],
                    'losses': franchise['h2hl']
                }
            )


def import_players():
    url = BASE_URL + '?TYPE=rosters&L=76173&APIKEY=&FRANCHISE=&JSON=1'
    res = requests.get(url).json()
    franchises = res['rosters']['franchise']
    for franchise in franchises:
        id = franchise['id']
        team, _ = models.Team.objects.get_or_create(mfl_id=id)
        for player in franchise['player']:
            player_url = BASE_URL + '?TYPE=playerProfile&P={}&JSON=1'.format(
                player['id']
            )
            player_res = requests.get(player_url).json()
            profile = player_res['playerProfile']
            name_team_pos = profile['name']
            first_name = ' '.join(
                name_team_pos.split(',')[1].strip().split(' ')[:-2]
            )
            last_name = name_team_pos.split(',')[0]
            position = name_team_pos.split(',')[1].strip().split(' ')[-1]
            adp = profile['player']['adp']
            if adp == 'N/A':
                adp = 999
            player_obj, _ = models.Player.objects.update_or_create(
                team=team,
                name=first_name + ' ' + last_name,
                mfl_id=player['id'],
                position=position,
                defaults={
                    'adp': adp,
                }
            )
            find_origin(player_obj, player['id'])


def find_origin(player, mfl_id):
    base = 'http://www74.myfantasyleague.com/2019/'
    url = '{}player_history?L=76173&PLAYERS={}'.format(
        base,
        mfl_id,
    )
    res = requests.get(url)
    tree = lxml.html.fromstring(res.text)
    table = tree.xpath('//table')[1]
    rows = table.xpath('tbody')[0].xpath('tr')[1:]
    for row in rows:
        year = row.xpath('td')[0].text_content()
        type_string = row.xpath('td')[2].text_content()
        print(type_string)
        if type_string.startswith('Won at auction'):
            player.auction_price = type_string.split('$')[1].strip()
            player.acquired = 'Startup Draft'
        elif type_string.startswith('Acquired via waivers'):
            try:
                player.waiver_price = type_string.split('$')[1].strip()
            except IndexError:
                player.waiver_price = 'FA'
            player.acquired = '{} Waivers'.format(year)
        elif type_string.startswith('Drafted at'):
            player.rookie_pick = type_string.split('pick')[1].strip()
            player.acquired = '{} Rookie Draft'.format(year)
            if int(year) == 2019:
                player.is_rookie = True
        elif type_string.startswith('Acquired in trade with'):
            player.acquired = '{} Trade'.format(year)
        elif type_string.startswith('Acquired via Free Agent'):
            player.acquired = '{} Free Agency'.format(year)
            player.waiver_price = 'FA'
        else:
            continue
        player.save()
        break
