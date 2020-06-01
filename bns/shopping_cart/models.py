# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from localflavor.us.models import USStateField
from django.contrib.auth.models import User
from listings.models import Post

class Cart(models.Model):
    buyer = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    final_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100) 
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f' {self.buyer} order'

