from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from user_profile.models import Profile
import datetime

class createListing(forms.Form):
    class Meta:
        model = Post
        fields = ['title', 'date', 'price', 'description']

    title = forms.CharField(max_length=500)
    date = forms.DateTimeField(initial=datetime.datetime.now())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))


    

    