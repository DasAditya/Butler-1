from django.conf.urls import url, include
from . import views

app_name = 'home'


urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/register/
    url(r'^register/$', views.register, name='register'),

    # /home/login/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /home/login/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /home/houseonrent/
    # url(r'^houseonrent/', include('houseonrent.urls'), name='houseonrent'),

]
