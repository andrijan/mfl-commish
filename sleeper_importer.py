import requests

from core import models

"""
stats_url = "https://api.sleeper.app/stats/nfl/2020?season_type=regular&position[]=DEF&position[]=QB&position[]=RB&position[]=TE&position[]=WR&order_by=pts_dynasty_half_ppr"
stats_response = requests.get(stats_url).json()
"""

projectsions_url = "https://api.sleeper.app/projections/nfl/2021?season_type=regular&position[]=DEF&position[]=QB&position[]=RB&position[]=TE&position[]=WR&order_by=pts_dynasty_half_ppr"
projections_response = requests.get(projectsions_url).json()
players = {
    projection['player_id']: projection for projection in projections_response
}

rosters_url = "https://api.sleeper.app/v1/league/650006508892954624/rosters"
rosters_response = requests.get(rosters_url).json()

for roster in rosters_response:
    team = models.Team.objects.get(sleeper_id=roster['roster_id'], year=2021)
    for player in roster['players']:
        projection_player = players[player]
        try:
            db_player = models.Player.objects.get(
                name=f"{projection_player['player']['first_name']} {projection_player['player']['last_name']}",
                team__year=2021,
            )
        except models.Player.DoesNotExist:
            continue
        db_player.adp = projection_player['stats']['adp_half_ppr']
        if db_player.team.sleeper_id != roster['roster_id']:
            db_player.team = team
        db_player.save()
