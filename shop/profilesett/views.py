from django.shortcuts import render
from registration.backends.simple.views import RegistrationView

from .models import UserProfile
# Create your views here.
class MyRegistrationView(RegistrationView):
    def get_success_url(request, user):
        return '/store/'
