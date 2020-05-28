# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django_countries.fields import CountryField
from localflavor.us.models import USStateField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_picture')
    country = CountryField()
    states = USStateField(null=True, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    bio = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.user.username} Profile'
    

    