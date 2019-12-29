from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('login',views.login,name = 'login'),
    path('playgame',views.play,name = 'play'),
    path('index2',views.index2,name = 'index2'),
    path('leaderboard',views.leaderboard,name = 'leaderboard'),

]