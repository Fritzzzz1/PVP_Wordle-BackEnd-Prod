from django.urls import path
from players.views import player_list, player_detail, player_create
from games.views import player_game_list
from rest_framework_simplejwt import views as jwt_views
from .views import GetToken

app_name = 'players'
urlpatterns = [
    path('', player_list, name='player-list'),
    path('<player_id>', player_detail, name='player-detail'),
    path('create/', player_create, name='player-create'),
    path('<int:player_id>/games/', player_game_list, name='player-game-list'),
    path('token/', GetToken.as_view(), name='token-obtain-pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
]
