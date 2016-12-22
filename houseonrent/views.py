import json
import requests
import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from restaurants.forms import RestSearchForm
from .models import House, Picture, BookmarkHouse
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
            House.objects.all().delete()

            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc.replace(" ", "+") + \
                  "&key=AIzaSyAzdZVMQeq3WZFbeO7wGZ9Un49xSwbdJiU"
            r1 = requests.get(url)
            for p in r1.json()['results']:
                lati = p['geometry']['location']['lat']
                longi = p['geometry']['location']['lng']

            url1 = 'https://ssl.hailyo.com/1.01/get/price'
            payload = {'long': str(longi), 'lat': str(lati), 'gcm_id': '8389902', 'locality': 'powai',
                       'platform': 'android', 'user_id': 'adfhuosrghohg', 'device': 'hdhesfhu', 'property_type': 'home'}
            headers = {'content-type': 'application/json'}
            payload_json = json.dumps(payload)
            r = requests.post(url1, data=payload_json, headers=headers)

            for p in r.json()['responseData']['buildings']:
                a = House()
                a.house_title = p['name']
                a.latitude = p['loc'][1]
                a.longitude = p['loc'][0]
                a.rent_price = p['or_psf']
                a.advance_pymt = p['ll_pm']
                a.config = p['config']
                addrUrl = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(p['loc'][1]) + "," + \
                          str(p['loc'][0]) + "&sensor=true"
                t = requests.get(addrUrl)
                a.address = t.json()['results'][0]['formatted_address']
                rnd_index = random.randint(0, Picture.objects.all().count()-1)
                temp = Picture.objects.all()[rnd_index]
                a.house_pic = temp.house_thumb
                if request.user.is_authenticated():
                    temp = BookmarkHouse.objects.filter(latitude=a.latitude, user=request.user).count()
                    if temp != 0:
                        a.is_bookmarked = True
                a.save()

            houses = House.objects.all()
            context = {'houses': houses,
                       'base_template': base,
                       'form': form
                       }
            return render(request, 'houseonrent/index.html', context)
    else:
        form = RestSearchForm()
        houses = House.objects.all()
        if request.user.is_authenticated():
            for h in houses:
                temp = BookmarkHouse.objects.filter(latitude=h.latitude, user=request.user).count()
                if temp != 0:
                    h.is_bookmarked = True
                else:
                    h.is_bookmarked = False

        context = {'houses': houses,
                   'form': form,
                   'base_template': base, }
    return render(request, 'houseonrent/index.html', context)


def detail(request, pk):
    house = House.objects.get(pk=pk)
    context = {'house': house}
    return render(request, 'houseonrent/detail.html', context)


def bookmark_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    try:
        temp = BookmarkHouse.objects.filter(latitude=house.latitude, user=request.user).count()
        if temp == 0:
            a = BookmarkHouse()
            a.user = request.user
            a.house_title = house.house_title
            a.latitude = house.latitude
            a.longitude = house.longitude
            a.rent_price = house.rent_price
            a.advance_pymt = house.advance_pymt
            a.config = house.config
            a.address = house.address
            a.house_pic = house.house_pic
            a.save()
        else:
            if house.is_bookmarked:
                house.is_bookmarked = False
            else:
                house.is_bookmarked = True
            BookmarkHouse.objects.filter(latitude=house.latitude, user=request.user).delete()
    except (KeyError, BookmarkHouse.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def delete_house(request, pk):
    house = get_object_or_404(BookmarkHouse, pk=pk)
    temp = House.objects.filter(latitude=house.latitude).count()
    if temp != 0:
        temp = House.objects.filter(latitude=house.latitude)[0]
        if temp.is_bookmarked:
            temp.is_bookmarked = False
        else:
            temp.is_bookmarked = True
    house.delete()
    return favorites(request)


def search(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    form = RestSearchForm()
    houses = House.objects.all()
    query = request.GET.get("q")
    if query:
        houses = houses.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(config__icontains=query) |
            Q(rent_price__icontains=query)
        ).distinct()
        context = {'houses': houses,
                   'form': form,
                   'base_template': base, }
        return render(request, 'houseonrent/index.html', context)
    else:
        context = {'houses': houses,
                   'form': form,
                   'base_template': base, }
        return render(request, 'houseonrent/index.html', context)




# for finding address from lati, longi
# url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=19.115638,72.900831&sensor=true"
# r = requests.get(url)
# r.json()
# print r.json()['results'][1]['formatted_address']

# street view image api = AIzaSyCf9Vv1Wg4x6v-KXU5NTfNO9cDOzu6dRzk
# https://maps.googleapis.com/maps/api/streetview?size=400x400&location=19.115638,72.900831&fov=90&heading=235&pitch=10&key=AIzaSyCf9Vv1Wg4x6v-KXU5NTfNO9cDOzu6dRzk