from django import forms
from registration.forms import RegistrationForm

class UserProfileRegistrationForm(RegistrationForm):
    country=forms.CharField(max_length=64)
    
