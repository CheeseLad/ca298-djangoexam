from django.shortcuts import render, get_object_or_404
import random
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'index.html')

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')




class UserLoginView(LoginView):
    template_name='login.html'


def logout_user(request):
    logout(request)
    return redirect("/")


def all_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games':games})

def all_platforms(request):
    platforms = Platform.objects.all()
    return render(request, 'platforms.html', {'platforms':platforms})


def single_game(request, gameid):
    game = get_object_or_404(Game, id=gameid)
    return render(request, 'game.html', {'game':game})


def single_platform(request, consoleid):
    all_games = Game.objects.filter(platform=consoleid)
    return render(request, 'games.html', {'games':all_games})


@login_required
def create_game(request):
    user = request.user
    if not user.is_superuser:
        return redirect("/")

    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save()
            return render(request, 'message.html', {'message.html': f"{new_game.name} created successfully"})
        else:
            return render(request, 'create_game.html', {'form':form})
    else:
        form = GameForm()
        return render(request, 'create_game.html', {'form': form})
    

@login_required
def buy_game(request, gameid):
    game = get_object_or_404(Game, id=gameid)
    user = request.user
    if game.stock == 0:
        return render(request, 'message.html', {'message': f"Sorry, {game.name} is out of stock"})
    elif game.stock >= 1:
            newGameUser = GameUser.objects.create(game=game, user=user)
            newGameUser.save()
            game.stock -= 1
            game.save()
            return render(request, 'confirmation.html', {'game': game, 'gameuser': newGameUser})
    
@login_required
def basket(request):
    user = request.user
    games = GameUser.objects.filter(user=user)
    total = 0
    for game in games:
        total += game.game.price
    return render(request, 'basket.html', {'orders':games, 'total':total})