# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return f"Game on {self.date}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shot(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    points = models.IntegerField()
    shooting_foul_drawn = models.BooleanField(default=False)
    shot_loc_x = models.FloatField()
    shot_loc_y = models.FloatField()
    action_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.action_type} shot by {self.player.name} in game {self.game.id}"
