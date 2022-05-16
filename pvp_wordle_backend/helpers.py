from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from players.models import Player
from enum import Enum


class SerializerResponse(Enum):
    single_item_success = 0
    many_items_success = 1


def check_and_save_serializer(data, serializer_class, context=None):
    if context and context.get("password"):
        try:
            validate_password(data['password'])
        except ValidationError as e:
            return e

    serializer = serializer_class(context and context.get("args"), data=data,
                                  many=True if context and context.get("many") else False)
    if serializer.is_valid():
        new_obj = serializer.save()

        if isinstance(new_obj, list):
            return SerializerResponse.many_items_success.value

        return new_obj.pk
    else:
        return serializer.errors


def check_and_save_new_player(data):
    try:
        validate_password(data['password'])
    except ValidationError as e:
        return e

    try:
        player = Player.objects.create_user(**data)
        player.save()
    except IntegrityError as e:
        return e.args

    return SerializerResponse.single_item_success.value
