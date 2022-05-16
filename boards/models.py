from django.db import models
from games.models import Game


class Board(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="board")

