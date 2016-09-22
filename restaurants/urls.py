from django.conf.urls import url, include
from . import views

app_name = 'restaurants'

urlpatterns = [
    # /restaurants/
    #url(r'^$', views.search, name='search'),

    # /restaurants/index/
    url(r'^$', views.index, name='index'),
]
