from rest_framework import serializers
from .models import Player
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('pk', 'username', 'password', 'score')
        extra_kwargs = {"password": {"write_only": True}}


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data.update([('refresh', str(refresh)),
                     ('access', str(refresh.access_token)),
                     ('player_id', self.user.pk),
                     ('username', self.user.username)])

        return data
