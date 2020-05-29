from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from listings.models import Post
import datetime

class createUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

    email = forms.CharField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    def __init__(self, *args, **kwargs):
        super(createUser, self).__init__(*args, **kwargs)
        for field_name in ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'):
            self.fields[field_name].help_text = ''

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
            }
    
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
            }
    ))

    fields = ['username', 'password']

class updateUserInfo(forms.ModelForm):
     
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    email = forms.CharField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    def __init__(self, *args, **kwargs):
        super(updateUserInfo, self).__init__(*args, **kwargs)
        for field_name in ('username', 'email', 'first_name', 'last_name'):
            self.fields[field_name].help_text = ''

class updateProfileInfo(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'country', 'states', 'city', 'bio']

        
    


