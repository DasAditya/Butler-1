from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^houseonrent/', include('houseonrent.urls')),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^forums/', include('forums.urls')),
    url(r'^homeservices/', include('homeservices.urls')),
    url(r'^furnitures/', include('furnitures.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

