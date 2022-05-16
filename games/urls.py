from django.urls import path
from games.views import game_list
from .views import game_detail

app_name = 'games'
urlpatterns = [
    path('', game_list, name='game-list'),
    path('<int:game_id>', game_detail, name='game-detail')
]
