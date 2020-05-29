# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from localflavor.us.models import USStateField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_picture')
    country = CountryField()
    states = USStateField(null=True, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    bio = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.user.username} Profile'
    

    