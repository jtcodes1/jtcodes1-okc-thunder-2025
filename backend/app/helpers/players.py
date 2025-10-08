# app/helpers/players.py
from rest_framework.views import APIView
from rest_framework.response import Response
from app.dbmodels import models

# ---------- FUNCTIONS YOU ALREADY HAVE ----------

def get_player_summary_stats(player_id: int):
    player = models.Player.objects.get(pk=player_id)
    shots = models.Shot.objects.filter(player=player)

    summary = {
        "playerID": player_id,
        "totalPoints": sum(shot.points for shot in shots),
        "totalShotAttempts": shots.count(),
        "actions": {}
    }

    for shot in shots:
        action = shot.action_type
        if action not in summary["actions"]:
            summary["actions"][action] = {"count": 0, "points": 0}
        summary["actions"][action]["count"] += 1
        summary["actions"][action]["points"] += shot.points

    return summary

def get_ranks(player_id: int, player_summary: dict):
    all_players = models.Player.objects.all()
    current_player = models.Player.objects.get(id=player_id)
    current_player_shots = current_player.shot_set.all()

    total_shot_attempts_rank = sum(
        1 for p in all_players if p.shot_set.count() > len(current_player_shots)
    ) + 1

    total_points_rank = sum(
        1 for p in all_players if sum(s.points for s in p.shot_set.all()) > sum(s.points for s in current_player_shots)
    ) + 1

    # Example for other stats
    total_passes_rank = sum(
        1 for p in all_players if player_summary.get("totalPasses", 0) < player_summary.get("totalPasses", 0)
    ) + 1

    return {
        "totalShotAttemptsRank": total_shot_attempts_rank,
        "totalPointsRank": total_points_rank,
        "totalPassesRank": total_passes_rank,
    }

# ---------- API VIEWS ----------

class PlayerSummary(APIView):
    def get(self, request, playerID):
        summary = get_player_summary_stats(int(playerID))
        ranks = get_ranks(int(playerID), summary)
        summary['ranks'] = ranks
        return Response(summary)

class AllPlayersSummary(APIView):
    def get(self, request):
        all_players = models.Player.objects.all()
        data = []
        for player in all_players:
            summary = get_player_summary_stats(player.id)
            ranks = get_ranks(player.id, summary)
            summary['ranks'] = ranks
            data.append(summary)
        return Response(data)
