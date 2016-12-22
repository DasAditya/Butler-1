from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from restaurants.models import BookmarkRest
from houseonrent.models import BookmarkHouse
from homeservices.models import BookmarkHomeservices
from furnitures.models import BookmarkFurniture
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import random
from .models import OTP
from django.contrib.auth.models import User


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
        to = str(form.cleaned_data['email'])
        user.set_password(password)
        otp=random.randint(1111,9999)
        user.save()
        a = OTP()
        a.user = user
        a.otp_assigned = otp
        a.save()
        user = authenticate(username=username, password=password)
        subject, from_email = 'Welcome To The Butler', ''
        text_content = 'Thank you for Registering'
        #context = Context({'user_name': username,'address': to,'otp':otp})
        context ={'user_name': username,'address': to,'otp':otp,'fname':user.first_name}
        htmly = get_template('home/green.html')
        html_content = htmly.render(context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        if user is not None:
            if user.is_active:
                #login(request, user)
                return render(request, 'home/opt.html', {'user': user})
    return render(request, 'home/register.html', {'form': form})


def otp_verify(request, pk):
    us = get_object_or_404(User, pk=pk)
    print us
    otp = get_object_or_404(OTP, user=us)
    otp.otp_entered= request.POST['otp_entered']
    b=str(otp.otp_entered)
    c=str(otp.otp_assigned)
    print otp.otp_entered
    print otp.otp_assigned
    otp.save()
    us.backend = 'django.contrib.auth.backends.ModelBackend'
    if c==b:
        login(request, us)
        otp.otp_verified=True
        otp.save()
        return render(request, 'home/index.html', {'base_template': "home/base_logged_in.html"})
    else:
        return render(request, 'home/opt.html', {'base_template': "home/base_logged_in.html", 'user': us})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        otp = get_object_or_404(OTP, user=user)
        if not otp.otp_verified:
            return render(request, 'home/opt.html', {'base_template': "home/base_logged_in.html", 'user': user})
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
    homeservices=BookmarkHomeservices.objects.filter(user=request.user)
    furnitures=BookmarkFurniture.objects.filter(user=request.user)
    #to = 'adityadas96@gmail.com'
    #to=str(request.user.email)
    context = {'restaurants': restaurants,
               'houses': houses,
               'homeservices': homeservices,
               'furnitures': furnitures,
               }
    # subject, from_email = 'Bookmarked Contents for '+request.user.username, 'thebutlersite@gmail.com'
    # text_content = 'Thank you for Registering'
    #
    # htmly = get_template('home/favorites1.html')
    # html_content = htmly.render(context)
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    return render(request, 'home/favorites.html', context)


def send_favorites(request):
    restaurants = BookmarkRest.objects.filter(user=request.user)
    houses = BookmarkHouse.objects.filter(user=request.user)
    homeservices = BookmarkHomeservices.objects.filter(user=request.user)
    furnitures = BookmarkFurniture.objects.filter(user=request.user)
    # to = 'adityadas96@gmail.com'
    #to = str(request.user.email)
    to = request.POST['email']
    context = {'restaurants': restaurants,
               'houses': houses,
               'homeservices': homeservices,
               'furnitures': furnitures,
               'fname': request.user.first_name,
               }
    print request.user.last_name
    subject, from_email = 'Bookmarked Contents from ' + request.user.first_name, 'thebutlersite@gmail.com'
    text_content = 'Thank you for Registering'

    htmly = get_template('home/favorites1.html')
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'home/favorites.html', context)

def about(request):
    if request.user.is_authenticated():
        base = "home/base_logged_in.html"
    else:
        base = "home/base_visitor.html"
    context = {'base_template': base}
    return render(request, 'home/about.html', context)
