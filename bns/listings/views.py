from django.shortcuts import render, redirect
from .forms import createListing
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def addPost(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    if request.method == "POST":
        form = createListing(request.POST)
        if form.is_valid():

            # saves a new post instance from Post data
            form.save()

    # Instance of form
    form = createListing()
    context = {'form':form}
    return render(request, 'listings/addPost.html', context)

#method for submitting form data into database
def listing_submission(request):
    print('form was submitted')
    messages.success(request, f'You have posted a new item.')
    #submitting data into database
    title = request.POST["title"]
    date = request.POST["date"]
    price = request.POST["price"]
    description = request.POST["description"]

    post = Post(title=title, date=date, price=price, description=description)
    post.save()
    form = createListing()
    context = {'form': form}
    return render(request, 'listings/addPost.html', context)