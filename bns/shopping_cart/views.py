# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'shopping_cart/cart.html')