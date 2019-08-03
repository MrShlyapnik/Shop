from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from .forms import UserProfileRegistrationForm
from .models import UserProfile
# Create your views here.
class MyRegistrationView(RegistrationView):
    form=UserProfileRegistrationForm
    us_copy=0
    def register(self, request, form):
        new_user=super(MyRegistrationView, self).register(request, form)
        user_profile=UserProfile()
        user_profile.user=new_user
        user_profile.country=form.cleaned_data['country']
        user_profile.save()
        us_copy=user_profile
        return user_profile
    def get_success_url(request, user):
        return '/store/'
    def get(self, request, *argw, **kwargs):
        return render(request, 'registration/registration_form.html', {'form': us_copy})
