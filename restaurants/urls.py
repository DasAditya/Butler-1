from django.conf.urls import url, include
from . import views

app_name = 'restaurants'

urlpatterns = [

    # /restaurants/
    url(r'^$', views.index, name='index'),

    # /restaurants/search/
    url(r'^search/$', views.search, name='search'),

    # /restaurants/rest_id/delete_rest/
    url(r'^(?P<pk>[0-9]+)/delete_rest/$', views.delete_rest, name='delete_rest'),

    # /home/restaurants/rest_id/bookmark_resto
    url(r'^(?P<pk>[0-9]+)/bookmark_resto/$', views.bookmark_resto, name='bookmark_resto'),

]
