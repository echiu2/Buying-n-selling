# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart(request):
    cart = Cart.objects.all()
    context = {'Cart': cart}
    return render(request, 'shopping_cart/cart.html', context)