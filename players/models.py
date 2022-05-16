from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    score = models.BigIntegerField(null=True, default=0)

