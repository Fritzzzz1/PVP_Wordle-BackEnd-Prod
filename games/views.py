from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from players.models import Player
from .serializer import GameSerializer
from .models import Game
from games.helpers import check_and_save_game, get_game_attempts
from django.shortcuts import get_object_or_404


@permission_classes([AllowAny])
@api_view(['GET'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()[::-1][:10]
        player_dict = {game.player.pk: game.player.username for game in games}

        serializer = GameSerializer(games, many=True)
        return Response([player_dict, serializer.data])

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def player_game_list(request, player_id):
    player = get_object_or_404(Player, pk=player_id)

    if request.method == 'GET':
        games = player.game.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        game_pk_or_errors = check_and_save_game(request.data, player_id)

        if type(game_pk_or_errors) is not int:
            return Response(game_pk_or_errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            player.score += Game.objects.get(pk=game_pk_or_errors).score
            player.save()
            return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
@api_view(['GET'])
def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    serializer = GameSerializer(game)
    attempts = get_game_attempts(game_id)

    return Response([serializer.data, attempts])

