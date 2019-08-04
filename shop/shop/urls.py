from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^store/', include('products.urls')),
    url(r'^accounts/', include('profilesett.urls')),
#url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
]
