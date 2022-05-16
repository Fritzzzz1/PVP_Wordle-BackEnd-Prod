from django.db import models
from pvp_wordle_backend.settings import AUTH_USER_MODEL as Player


class Game(models.Model):
    player = models.ForeignKey(Player, default="guest", on_delete=models.SET_DEFAULT, related_name="game")
    secret = models.CharField(max_length=5)
    duration = models.DurationField(null=True, blank=True)
    won = models.BooleanField()
    score = models.SmallIntegerField(default=0)
