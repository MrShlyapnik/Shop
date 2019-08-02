from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from registration.backends.simple.views import RegistrationView
class MyRegistrationView(RegistrationView):
    def get_success_url(request, user):
        return '/store/'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^store', include('products.urls')),
    url(r'^user', include('profilesett.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
