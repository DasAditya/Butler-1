from django.shortcuts import render
import requests
from .models import Restaurant
from .forms import RestSearchForm


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
            # geolocator=Nominatim()
            # lati=0
            # while (lati==0): AIzaSyAzdZVMQeq3WZFbeO7wGZ9Un49xSwbdJiU
            # location = geolocator.geocode(loc,timeout=1000)
            # lati=location.latitude
            # longi=location.longitude

            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc.replace(" ","+") + \
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
                # r = requests.get('https://developers.zomato.com/api/v2.1/geocode?lat=41.10867962215988&lon=29.01834726333618',headers={'user_key: 1932a0b77f3352d89db1b1cc3d3a04e9' ,'Accept: application/json'})
                # json = r.json()

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
                    a.user_rating_agg = p['restaurant']['user_rating']['aggregate_rating']
                    a.user_rating_vote = p['restaurant']['user_rating']['votes']
                    a.res_id = p['restaurant']['R']['res_id']
                    a.save()
                offset += 20

            restaurants = Restaurant.objects.all()
            #         serializer = EmbedSerializer(data=json)
            #         serializer.is_valid()
            #         embed = serializer.save()
            context = {'restaurants': restaurants,
                       'base_template': base, }
            return render(request, 'restaurants/index.html', context)
    else:
        form = RestSearchForm()
        restaurants = Restaurant.objects.all()
        context = {'restaurants': restaurants,
                 'form': form,
                 'base_template': base, }
    return render(request, 'restaurants/index.html', context)
