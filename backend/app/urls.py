"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path
from .helpers import players
from django.http import JsonResponse

# Simple root view to stop 404 at /
def root_view(request):
    return JsonResponse({"message": "Welcome to OKC API!"})

urlpatterns = [
    re_path(r'^api/v1/playerSummary/(?P<playerID>[0-9]+)$', players.PlayerSummary.as_view(), name='player_summary'),
    re_path(r'^api/v1/allPlayersSummary$', players.AllPlayersSummary.as_view(), name='all_players_summary'),
    re_path(r'^$', root_view),  # Root route
]

