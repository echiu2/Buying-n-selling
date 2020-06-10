# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from localflavor.us.models import USStateField
from django.contrib.auth.models import User
from listings.models import Post

# class CartItem(models.Model):
#     product =models.OneToOneField(Post, on_delete=models.SET_NULL, null=True)
    
#     def __str__(self):
#         return self.product.title

class Cart(models.Model):
    buyer = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    items = models.ManyToManyField(Post, null=True, blank=True)
    is_ordered = models.BooleanField(default=False)
    # product = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    final_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100) 
    date_ordered = models.DateTimeField(auto_now=True)
    # amount = models.PositiveIntegerField(default=0)

    # def get_cart_items(self):
    #     return self.items.all()

    # def get_cart_total(self):
    #     return sum([item.product.price for item in self.items.all()])

    # def __str__(self):
    #     return f' {self.buyer} order'

    def __str__(self):
        return "Cart id: %s" %(self.id)


