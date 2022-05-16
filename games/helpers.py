from pvp_wordle_backend.helpers import check_and_save_serializer
from boards.serializer import BoardSerializer
from attempts.serializer import AttemptSerializer
from games.serializer import GameSerializer
from boards.models import Board


def check_and_save_game(request_data, player_id):
    request_data['player'] = player_id
    game_pk_or_errors = check_and_save_serializer(request_data, GameSerializer)

    if not isinstance(game_pk_or_errors, int):
        return game_pk_or_errors

    board_pk_or_errors = check_and_save_serializer({'game': game_pk_or_errors}, BoardSerializer)

    if not isinstance(board_pk_or_errors, int):
        return board_pk_or_errors

    words = request_data.get('attempts')
    if words:
        attempts = [{'board': board_pk_or_errors, 'word': words[i - 1]} for i in range(1, len(words) + 1)]

        attempts_errors = check_and_save_serializer(attempts, AttemptSerializer, {"many": True})
        if not isinstance(attempts_errors, int):
            return attempts_errors

    return game_pk_or_errors


def get_game_attempts(game_id):
    board = Board.objects.get(game=game_id)
    attempts = board.attempt.all().values_list('word', flat=True)

    attempt_dict = {"Attempt" + f"{i}": attempts[i - 1] for i in range(1, len(attempts) + 1)}

    return attempt_dict
