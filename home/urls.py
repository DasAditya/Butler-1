from django.conf.urls import url, include
from . import views

app_name = 'home'


urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/houseonrent/
    # url(r'^houseonrent/', include('houseonrent.urls'), name='houseonrent'),

]
