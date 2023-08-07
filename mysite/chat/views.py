from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from unidecode import unidecode
from .models import *
from .forms import *


def main_page(request):
    rooms = Room.objects.filter(Q(is_public=True) | Q(participants=request.user))
    return render(request, "chat/main_page.html", {'form': UserLoginForm, 'rooms': rooms})


@login_required
def room(request, room_name=None):
    if room_name == None:
        room_name = request.GET.get('room_name')

    try:
        room = Room.objects.get(title=room_name, is_banned=False)
        if room.is_public or request.user in room.participants.all():
            return render(request, "chat/room.html", {"room_name": room_name, 'user': request.user, 'room': room})
        else:
            return redirect('main_page')
    except:
        return redirect('main_page')


@login_required
def profile(request, slug=None):
    if slug:
        user = CustomUser.objects.get(slug=slug)
        if user.is_banned:
            return redirect('ЗАБАНЕН')
    else:
        user = request.user
    return render(request, 'user_profile/profile.html', {'user': user})


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.slug = unidecode(user.username).lower().replace(' ', '-')
            user.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authorization/authorization.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('main_page')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserLoginForm()
    return render(request, 'authorization/authorization.html', {'form': form})
