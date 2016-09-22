from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import House, BookmarkHouse


def index(request):
    all_houses = House.objects.all()
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
<<<<<<< HEAD
    context = {'houses': all_houses,
               'base_template': base, }
=======
    context = {}
    context = {'houses': all_houses,
               'base_template': base,}
>>>>>>> origin/master
    return render(request, 'houseonrent/index.html', context)


def detail(request, pk):
    house = House.objects.get(pk=pk)
    context = {'house': house}
    return render(request, 'houseonrent/detail.html', context)

<<<<<<< HEAD

def bookmark_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    try:
        a = BookmarkHouse()
        a.user = request.user
        a.house = house
        a.save()
    except (KeyError, BookmarkHouse.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


# def bookmarks(request):
#     houses = BookmarkHouse.objects.filter(user=request.user)
=======
>>>>>>> origin/master
