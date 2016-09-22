from django.conf.urls import url, include
from . import views

app_name = 'houseonrent'

urlpatterns = [
    # /home/houseonrent/
    url(r'^$', views.index, name='index'),

    # /home/houseonrent/house_id/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # /home/houseonrent/house_id/bookmark_house
    url(r'^(?P<pk>[0-9]+)/bookmark_house/$', views.bookmark_house, name='bookmark_house'),
]
