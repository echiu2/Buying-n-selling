# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Cart, Post
from user_profile.models import Profile

# Create your views here.
def cart(request):    
    try:
        session_id = request.session['cart_id']
    except:
        session_id = None
    if session_id:
        cart = Cart.objects.get(id=session_id)
        current_user = request.user
        cart.buyer = current_user
        cart.save()
        empty_message = "Your Shopping Cart is empty, please keep shopping."
        context = {
            'Cart': cart,
            'Empty_Message': empty_message
        }
    else:
        context={
            'Empty': True,
        }
    return render(request, 'shopping_cart/cart.html', context)

def update_cart(request, post_slug):
    # Using session for every user to have their own shopping cart. If user does not have a session id,
    # we create a new one for that user
    try:
        session_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        session_id = new_cart.id

    cart = Cart.objects.get(id=session_id)
    try:
        product = Post.objects.get(slug=post_slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    # Check if product exist in the cart, if not add it bc we have ManyToMany relationship
    if not product in cart.items.all():
        cart.items.add(product)
    else:
        cart.items.remove(product)

    subtotal = 0.00
    tax = 1.0875

    for item in cart.items.all():
        subtotal += float(item.price)
    
    finaltotal = subtotal * tax

    cart.subtotal = subtotal    
    cart.final_total = finaltotal

    #After calculating subtotal and final total, save the cart
    cart.save()

    return redirect(reverse("cart"))
