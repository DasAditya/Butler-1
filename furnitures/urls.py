from django.conf.urls import url, include
from . import views

app_name = 'furnitures'

urlpatterns = [
    # /home/furnitures/
    url(r'^$', views.index, name='index'),

    # /home/furnitures/id/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # /furnitures/search/
    url(r'^search/$', views.search, name='search'),

    # /home/furitures/id/bookmark_furniture
    url(r'^(?P<pk>[0-9]+)/bookmark_furniture/$', views.bookmark_furniture, name='bookmark_furniture'),

    # /home/furnitures/id/delete_furniture
    url(r'^(?P<pk>[0-9]+)/delete_furniture/$', views.delete_furniture, name='delete_furniture'),
]
