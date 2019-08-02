from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class IndexList(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/index.html')
