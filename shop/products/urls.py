from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from .views import IndexList
urlpatterns = [
    url(r'', IndexList.as_view())
]
