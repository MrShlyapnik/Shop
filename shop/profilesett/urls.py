from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from .views import MyRegistrationView
urlpatterns = [
url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^', include('registration.backends.simple.urls')),


]
