# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import createListing, createUser, loginForm
from .models import Post

# Create your views here.
def index(request):
    #Get all listings from database
    all_listings = Post.objects.all()
    context = {'Listings': all_listings}
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def shop(request):
    return render(request, 'myapp/shop.html')

def account(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    if request.method == "POST":
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
    context = {'form': form}
    return render(request, 'myapp/account.html', context)

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
    context = {'form': form}
    return render(request, 'myapp/account.html', context)

def cart(request):
    return render(request, 'myapp/cart.html')

def loginPage(request):
    form = loginForm()

    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrect!')

    context = {'form': form}
    return render(request, 'myapp/login.html', context)

def register(request):   
    form = createUser()
 
    if request.method == "POST":
        form = createUser(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password1 = form.cleaned_data['password1']
            # password2 = form.cleaned_data['password2']

            # Create that user by checking if username is not used using django auth
            form.save()
            # print(username, email, password1, password2)
            user = form.cleaned_data['username']
            messages.success(request, 'You have created an account for ' + user)
            return redirect("/")

    context = {'form': form}
    return render(request, 'myapp/register.html', context)