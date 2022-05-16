from django.db import models
from boards.models import Board


class Attempt(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="attempt")
    word = models.CharField(max_length=6)

