from django.shortcuts import render, get_object_or_404
import requests
from .models import Restaurant, BookmarkRest
from .forms import RestSearchForm
from django.http import JsonResponse
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
            Restaurant.objects.all().delete()

            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc.replace(" ", "+") + \
                  "&key=AIzaSyAzdZVMQeq3WZFbeO7wGZ9Un49xSwbdJiU"
            r1 = requests.get(url)
            for p in r1.json()['results']:
                lati = p['geometry']['location']['lat']
                longi = p['geometry']['location']['lng']

            offset = 0
            while offset != 60:

                locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/search?start=" + str(
                    offset) + "&lat=" + str(lati) + "&lon=" + str(longi) + "&radius=3000"
                header = {"User-agent": "curl/7.43.0", "Accept": "application/json",
                          "user_key": "1932a0b77f3352d89db1b1cc3d3a04e9"}
                r = requests.get(locationUrlFromLatLong, headers=header)

                for p in r.json()['restaurants']:
                    a = Restaurant()
                    a.restaurant_name = p['restaurant']['name']
                    a.location_address = p['restaurant']['location']['address']
                    a.location_locality = p['restaurant']['location']['locality']
                    a.location_city = p['restaurant']['location']['city']
                    a.location_latitude = p['restaurant']['location']['latitude']
                    a.location_longitude = p['restaurant']['location']['longitude']
                    a.restaurant_cuisine = p['restaurant']['cuisines']
                    a.restaurant_avgcostfor2 = p['restaurant']['average_cost_for_two']
                    a.restaurant_thumb = p['restaurant']['thumb']
                    if p['restaurant']['user_rating']['aggregate_rating'] == '0':
                        a.user_rating_agg = 3
                    else:
                        a.user_rating_agg = p['restaurant']['user_rating']['aggregate_rating']
                    if p['restaurant']['user_rating']['votes'] == '0':
                        a.user_rating_vote = 5
                    else:
                        print p['restaurant']['user_rating']['votes']
                        a.user_rating_vote = p['restaurant']['user_rating']['votes']
                    a.res_id = p['restaurant']['R']['res_id']
                    if request.user.is_authenticated():
                        temp = BookmarkRest.objects.filter(res_id=a.res_id, user=request.user).count()
                        if temp != 0:
                            a.is_bookmarked = True
                    a.save()
                offset += 20

            restaurants = Restaurant.objects.all()
            context = {'restaurants': restaurants,
                       'base_template': base,
                       'form': form
                       }
            return render(request, 'restaurants/index.html', context)
    else:
        form = RestSearchForm()
        restaurants = Restaurant.objects.all()
        if request.user.is_authenticated():
            for r in restaurants:
                temp = BookmarkRest.objects.filter(res_id=r.res_id, user=request.user).count()
                if temp != 0:
                    r.is_bookmarked = True
                else:
                    r.is_bookmarked = False

    context = {'restaurants': restaurants,
               'form': form,
               'base_template': base, }
    return render(request, 'restaurants/index.html', context)


def bookmark_resto(request, pk):
    rest = get_object_or_404(Restaurant, pk=pk)
    try:
        temp = BookmarkRest.objects.filter(res_id=rest.res_id, user=request.user).count()
        if temp == 0:
            a = BookmarkRest()
            a.user = request.user
            a.restaurant_name = rest.restaurant_name
            a.location_address = rest.location_address
            a.location_locality = rest.location_locality
            a.location_city = rest.location_city
            a.location_latitude = rest.location_latitude
            a.location_longitude = rest.location_longitude
            a.restaurant_cuisine = rest.restaurant_cuisine
            a.restaurant_avgcostfor2 = rest.restaurant_avgcostfor2
            a.restaurant_thumb = rest.restaurant_thumb
            a.user_rating_agg = rest.user_rating_agg
            a.user_rating_vote = rest.user_rating_vote
            a.res_id = rest.res_id
            a.save()
        else:
            if rest.is_bookmarked:
                rest.is_bookmarked = False
            else:
                rest.is_bookmarked = True
            BookmarkRest.objects.filter(res_id=rest.res_id, user=request.user).delete()
    except (KeyError, BookmarkRest.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def delete_rest(request, pk):
    rest = get_object_or_404(BookmarkRest, pk=pk)
    temp = Restaurant.objects.filter(res_id=rest.res_id).count()
    if temp != 0:
        temp = Restaurant.objects.filter(res_id=rest.res_id)[0]
        if temp.is_bookmarked:
            temp.is_bookmarked = False
        else:
            temp.is_bookmarked = True
    rest.delete()
    return favorites(request)


def search(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    form = RestSearchForm()
    restaurants = Restaurant.objects.all()
    query = request.GET.get("q")
    if query:
        restaurants = restaurants.filter(
            Q(restaurant_name__icontains=query) |
            Q(restaurant_cuisine__icontains=query)
        ).distinct()
        context = {'restaurants': restaurants,
                   'form': form,
                   'base_template': base, }
        return render(request, 'restaurants/index.html', context)
    else:
        context = {'restaurants': restaurants,
                   'form': form,
                   'base_template': base, }
        return render(request, 'restaurants/index.html', context)
