from django.shortcuts import render

from .models import House


def index(request):
    all_houses = House.objects.all()
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    context = {}
    context = {'houses': all_houses,
               'base_template': base,}
    return render(request, 'houseonrent/index.html', context)


def detail(request, pk):
    house = House.objects.get(pk=pk)
    context = {'house': house}
    return render(request, 'houseonrent/detail.html', context)

