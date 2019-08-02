from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('products.urls')),
    url(r'user', include('profilesett.urls'))
]
