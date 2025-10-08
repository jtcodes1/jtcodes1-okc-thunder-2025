import sys
import json
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # adds backend/ to path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()

from app.models import Team, Game, Player, Shot

# Load teams.json first if it exists
with open('raw_data/teams.json') as f:
    teams_data = json.load(f)

teams_dict = {}
for team in teams_data:
    obj, _ = Team.objects.get_or_create(name=team['name'])
    teams_dict[team['team_id']] = obj  # Map team_id from JSON to Team object

# Load games.json
with open('raw_data/games.json') as f:
    games_data = json.load(f)

games_dict = {}
for game in games_data:
    obj, _ = Game.objects.get_or_create(date=game['date'])
    games_dict[game['id']] = obj  # Map game_id from JSON to Game object

# Load players.json
with open('raw_data/players.json') as f:
    players_data = json.load(f)

for player in players_data:
    team_obj = teams_dict[player['team_id']]
    player_obj, _ = Player.objects.get_or_create(name=player['name'], team=team_obj)

    for shot in player['shots']:
        game_obj = games_dict[shot['game_id']]
        Shot.objects.update_or_create(
            player=player_obj,
            game=game_obj,
            shot_loc_x=shot['shot_loc_x'],
            shot_loc_y=shot['shot_loc_y'],
            action_type=shot['action_type'],
            defaults={
                'points': shot['points'],
                'shooting_foul_drawn': shot['shooting_foul_drawn']
            }
        )

print("Teams, Games, Players, and Shots loaded successfully.")