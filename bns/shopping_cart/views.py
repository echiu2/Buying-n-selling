# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Cart, Post

# Create your views here.
def cart(request):
    cart = Cart.objects.all()[0]
    context = {'Cart': cart}
    return render(request, 'shopping_cart/cart.html', context)

# def update_cart(requests, post_slug):
#     cart = Cart.objects.all()[0]
#     try:
#         product = Post.objects.get(slug=slug)
#     except: Product.DoesNotExist:
#         pass
#     except:
#         pass

#     if not product in cart.items.all():
#         cart.items.add(product)
#     else:
#         cart.items.remove(product)

#     return HttpResponseRedirect(reverse("cart"))
