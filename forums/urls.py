from django.conf.urls import url, include
from . import views

app_name = 'forums'


urlpatterns = [

    # /forums/
    url(r'^$', views.index, name='index'),

    # /forums/add_topic/
    url(r'^add_topic/$', views.add_topic, name='add_topic'),

    # /forums/add_topic/
    url(r'^add_topic/$', views.add_topic, name='add_topic'),

    # /forums/add_post/
    url(r'^(?P<pk>[0-9]+)/add_topic/$', views.add_post, name='add_post'),

]
