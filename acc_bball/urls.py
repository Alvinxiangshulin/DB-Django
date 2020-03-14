from django.urls import path
from acc_bball import views

urlpatterns = [
    path('createplayer/', views.createPlayer),
    path('createcolor/', views.createColor),
    path('createstate/', views.createState),
    path('createteam/', views.createTeam),
]
