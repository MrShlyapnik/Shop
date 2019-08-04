from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import ListView, DetailView
from .models import Product

from .views import IndexList, Towar
urlpatterns = [
url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Product, template_name="products/product.html")),
    url(r'$', IndexList.as_view()),

]
