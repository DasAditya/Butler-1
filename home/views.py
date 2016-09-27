from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from restaurants.models import BookmarkRest
from houseonrent.models import BookmarkHouse


def index(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    context = {'base_template': base}
    return render(request, 'home/index.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html', {'base_template': "home/base_logged_in.html"})
    return render(request, 'home/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/index.html', {'base_template': "home/base_logged_in.html"})
    return render(request, 'home/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)


def favorites(request):
    restaurants = BookmarkRest.objects.filter(user=request.user)
    houses = BookmarkHouse.objects.filter(user=request.user)
    context = {'restaurants': restaurants,
               'houses': houses}
    return render(request, 'home/favorites.html', context)
