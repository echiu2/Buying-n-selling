# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import createListing
from .models import Post

# Create your views here.
def index(request):
    #Get all listings from database
    all_listings = Post.objects.all()
    return render(request, 'myapp/home.html', {'Listings': all_listings})

def about(request):
    return render(request, 'myapp/about.html')

def shop(request):
    return render(request, 'myapp/shop.html')

def account(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    if request.method == "Post":
        form = createListing(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            # saves a new post instance from Post data
            form.save()

            print(title, date, price, description)

    # Instance of form
    form = createListing()
    return render(request, 'myapp/account.html', {'form': form})

#method for submitting form data into database
def listing_submission(request):
    print('form was submitted')
    #submitting data into database
    title = request.POST["title"]
    date = request.POST["date"]
    price = request.POST["price"]
    description = request.POST["description"]

    post = Post(title=title, date=date, price=price, description=description)
    post.save()
    form = createListing()
    return render(request, 'myapp/account.html', {'form': form})

def cart(request):
    return render(request, 'myapp/cart.html')