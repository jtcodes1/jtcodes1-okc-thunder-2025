# -*- coding: utf-8 -*-
import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from app.helpers.players import get_player_summary_stats, get_ranks

LOGGER = logging.getLogger('django')


class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data"""
        print(playerID)

        player_summary = get_player_summary_stats(player_id=playerID)
        player_summary = player_summary | get_ranks(player_id=playerID, player_summary=player_summary)

        return Response(player_summary)


class AllPlayersSummary(APIView):
    """Return summaries and ranks for all players"""

    def get(self, request):
        from app.dbmodels import models
        from app.helpers.players import get_player_summary_stats, get_ranks

        all_player_data = {}

        for player in models.Player.objects.all():
            summary = get_player_summary_stats(player.id)
            ranks = get_ranks(player.id, summary)
            all_player_data[player.name] = {
                "summary": summary,
                "ranks": ranks
            }

        return Response(all_player_data)