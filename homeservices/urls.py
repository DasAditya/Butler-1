from django.conf.urls import url, include
from . import views

app_name = 'homeservices'

urlpatterns = [
    # /home/houseonrent/
    url(r'^$', views.index, name='index'),

    # /home/houseonrent/house_id/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # /houseonrent/search/
    url(r'^search/$', views.search, name='search'),

    # /home/houseonrent/house_id/bookmark_homeservices
    url(r'^(?P<pk>[0-9]+)/bookmark_homeservices/$', views.bookmark_homeservices, name='bookmark_homeservices'),

    # /home/houseonrent/house_id/delete_homeservices
    url(r'^(?P<pk>[0-9]+)/delete_homeservices/$', views.delete_homeservices, name='delete_homeservices'),
]
