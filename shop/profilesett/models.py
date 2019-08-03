from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    country=models.CharField(max_length=64)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
