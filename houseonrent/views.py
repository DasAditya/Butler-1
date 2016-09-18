from django.shortcuts import render

from .models import House


def index(request):
    all_houses = House.objects.all()
    context = {'houses': all_houses}
    return render(request, 'houseonrent/index.html', context)

def detail(request, pk):
    house = House.objects.get(pk=pk)
    context = {'house': house}
    return render(request, 'houseonrent/detail.html', context)
