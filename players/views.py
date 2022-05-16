from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import PlayerSerializer, TokenSerializer
from .models import Player
from django.shortcuts import get_object_or_404
from pvp_wordle_backend.helpers import check_and_save_serializer, check_and_save_new_player
from rest_framework_simplejwt.views import TokenObtainPairView


class GetToken(TokenObtainPairView):
    serializer_class = TokenSerializer


@api_view(['GET'])
def player_list(request):
    players = Player.objects.all().exclude(username='guest').order_by('-score')[:10]
    serializer = PlayerSerializer(players, many=True)
    for player in serializer.data:
        player['games'] = len(Player.objects.get(pk=player['pk']).game.all())

    return Response(serializer.data)


@api_view(['POST'])
def player_create(request):
    player_pk_or_errors = check_and_save_new_player(request.data)

    if isinstance(player_pk_or_errors, int):
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(player_pk_or_errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
def player_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)

    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    elif request.method == 'PUT':
        errors = check_and_save_serializer(request.data, PlayerSerializer, {"args": player, "password": True})

        if type(errors) is not int:
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        player.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)

