from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class IndexList(ListView):
    def get(self, request, *args, **kwargs):
        model=Product
        context_object_name = 'products'
        objects=model.objects.all()
        return render(request, 'products/index.html',{
        'products': objects
        })
    def post(self, request, *args, **kwargs):
        return render(request, 'products/index.html')
