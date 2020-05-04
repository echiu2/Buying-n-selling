from django import forms 
import datetime

class createListing(forms.Form):
    title = forms.CharField(max_length=500)
    date = forms.DateTimeField(initial=datetime.datetime.now())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))