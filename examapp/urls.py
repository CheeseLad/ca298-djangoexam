from django.urls import path, include
from . import views
from .forms import * # add o imports at the top of the file

urlpatterns = [
    path('',views.index, name="index"),# mywebsite.com 
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('games', views.all_games, name="all_games"),
    path('platforms', views.all_platforms, name="all_platforms"),
    path('platform/<int:consoleid>', views.single_platform, name="single_platform"),
    path('game/<int:gameid>', views.single_game, name="single_game"),
    path('game/<int:gameid>/buy', views.buy_game, name="buy_game"),
    path('create_game', views.create_game, name="create_game"),
    path('basket', views.basket, name="basket"),
]