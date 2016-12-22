from django.conf.urls import url, include
from . import views

app_name = 'home'


urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),

    # /home/login/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /home/login/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /home/favorites/
    url(r'^favorites/$', views.favorites, name='favorites'),

    # /home/favorites/
    url(r'^send_favorites/$', views.send_favorites, name='send_favorites'),

    # /home/otp/
    url(r'^(?P<pk>[0-9]+)/otp/$', views.otp_verify, name='otp_verify'),

]
