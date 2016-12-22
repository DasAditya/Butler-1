import json
import requests
import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from restaurants.forms import RestSearchForm
from .models import Homeservices, Picture, BookmarkHomeservices
from django.db.models import Q
from home.views import favorites


def index(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    if request.method == "POST":
        form = RestSearchForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['location']
            Homeservices.objects.all().delete()

            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc.replace(" ", "+") + \
                  "&key=AIzaSyAzdZVMQeq3WZFbeO7wGZ9Un49xSwbdJiU"
            r1 = requests.get(url)
            for p in r1.json()['results']:
                lati = p['geometry']['location']['lat']
                longi = p['geometry']['location']['lng']
            count = 0
            types = ['Maid', 'Plumber', 'Electrician', 'Carpenter']
            print types[1]
            urlservices = ['https://maps.googleapis.com/maps/api/place/textsearch/json?query=maid+service+in+' + loc.replace(" ", "+") + '&radius=500000&key=AIzaSyAr5X1Qy5pTLhddd3_QjMb7IkklWiMw6CU',
                           'https://maps.googleapis.com/maps/api/place/textsearch/json?query=plumber+in+' + loc.replace(" ", "+") + '&radius=500000&key=AIzaSyAr5X1Qy5pTLhddd3_QjMb7IkklWiMw6CU',
                           'https://maps.googleapis.com/maps/api/place/textsearch/json?query=electrician+in+' + loc.replace(" ", "+") + '&radius=500000&key=AIzaSyAr5X1Qy5pTLhddd3_QjMb7IkklWiMw6CU',
                           'https://maps.googleapis.com/maps/api/place/textsearch/json?query=carpenter+in+' + loc.replace(" ", "+") + '&radius=500000&key=AIzaSyAr5X1Qy5pTLhddd3_QjMb7IkklWiMw6CU']
                # locationUrlFromLatLong = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=plumber+'+loc.replace(" ","+")+'&radius=500000&key=AIzaSyCpBaMrxTeqjNjn-_qgvft14AQdDllOrNo'
            for url in urlservices:
                r = requests.get(url)
                    # r = requests.get('https://developers.zomato.com/api/v2.1/geocode?lat=41.10867962215988&lon=29.01834726333618',headers={'user_key: 1932a0b77f3352d89db1b1cc3d3a04e9' ,'Accept: application/json'})
                    # json = r.json()

                for p in r.json()['results']:
                    a = Homeservices()
                    print types
                    a.type = types[count]
                    a.name = p['name']
                    a.address = p['formatted_address']
                    a.latitude = p['geometry']['location']['lat']
                    a.longitude = p['geometry']['location']['lng']
                    a.img = p['icon']
                    a.place_id = p['place_id']
                    a.save()
                    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+p['place_id']+'&key=AIzaSyAr5X1Qy5pTLhddd3_QjMb7IkklWiMw6CU'
                    r1 = requests.get(url)
                    if 'rating' in r1.json()['result']:
                        a.rating = r1.json()['result']['rating']
                    if 'international_phone_number' in r1.json()['result']:
                        a.contact = r1.json()['result']['international_phone_number']
                    if 'opening_hours' in r1.json()['result']:
                        a.open_now = r1.json()['result']['opening_hours']['open_now']
                        for p1 in r1.json()['result']['opening_hours']['periods']:
                            a.open_time = p1['open']['time']

                            a.close_time = p1['close']['time']
                    if request.user.is_authenticated():
                        temp = BookmarkHomeservices.objects.filter(place_id=a.place_id, user=request.user).count()
                        if temp != 0:
                            a.is_bookmarked = True
                    rnd_index = random.randint(0, Picture.objects.filter(type = types[count]).count() - 1)
                    temp = Picture.objects.filter(type = types[count])[rnd_index]
                    a.img = temp.homeservices_thumb
                    a.save()
                count=count+1

            homeservices = Homeservices.objects.all()

            context = {'homeservices': homeservices,
                       'base_template': base,
                       'form': form
                       }
            return render(request, 'homeservices/index.html', context)
    else:
        form = RestSearchForm()
        homeservices = Homeservices.objects.all()
        if request.user.is_authenticated():
            for h in homeservices:
                temp = BookmarkHomeservices.objects.filter(place_id=h.place_id, user=request.user).count()
                if temp != 0:
                    h.is_bookmarked = True
                else:
                    h.is_bookmarked = False

        context = {'homeservices': homeservices,
                   'form': form,
                   'base_template': base, }
    return render(request, 'homeservices/index.html', context)


def detail(request, pk):
    homeservices = Homeservices.objects.get(pk=pk)
    context = {'homeservices': homeservices}
    return render(request, 'homeservices/detail.html', context)


def bookmark_homeservices(request, pk):
    homeservices = get_object_or_404(Homeservices, pk=pk)
    try:
        temp = BookmarkHomeservices.objects.filter(place_id=homeservices.place_id, user=request.user).count()
        if temp == 0:
            a = BookmarkHomeservices()
            a.user = request.user
            a.name = homeservices.name
            a.address = homeservices.address
            a.latitude = homeservices.latitude
            a.longitude = homeservices.longitude
            a.img = homeservices.img
            a.place_id = homeservices.place_id
            a.rating = homeservices.rating
            a.open_now = homeservices.open_now
            a.open_time = homeservices.open_time
            a.close_time = homeservices.close_time
            a.contact = homeservices.contact
            a.type = homeservices.type
            a.save()
        else:
            if homeservices.is_bookmarked:
                homeservices.is_bookmarked = False
            else:
                homeservices.is_bookmarked = True
            BookmarkHomeservices.objects.filter(place_id=homeservices.place_id, user=request.user).delete()
    except (KeyError, BookmarkHomeservices.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def delete_homeservices(request, pk):
    homeservices = get_object_or_404(BookmarkHomeservices, pk=pk)
    temp = Homeservices.objects.filter(place_id=homeservices.place_id).count()
    if temp != 0:
        temp = Homeservices.objects.filter(place_id=homeservices.place_id)[0]
        if temp.is_bookmarked:
            temp.is_bookmarked = False
        else:
            temp.is_bookmarked = True
    homeservices.delete()
    return favorites(request)


def search(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    form = RestSearchForm()
    homeservices = Homeservices.objects.all()
    query = request.GET.get("q")
    if query:
        homeservices = homeservices.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(type__icontains=query)
        ).distinct()
        context = {'homeservices': homeservices,
                   'form': form,
                   'base_template': base, }
        return render(request, 'homeservices/index.html', context)
    else:
        context = {'homeservices': homeservices,
                   'form': form,
                   'base_template': base, }
        return render(request, 'homeservices/index.html', context)




# for finding address from lati, longi
# url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=19.115638,72.900831&sensor=true"
# r = requests.get(url)
# r.json()
# print r.json()['results'][1]['formatted_address']

# street view image api = AIzaSyCf9Vv1Wg4x6v-KXU5NTfNO9cDOzu6dRzk
# https://maps.googleapis.com/maps/api/streetview?size=400x400&location=19.115638,72.900831&fov=90&heading=235&pitch=10&key=AIzaSyCf9Vv1Wg4x6v-KXU5NTfNO9cDOzu6dRzk