from django import forms
from .models import Userinputmodel
from django.forms import DateInput
from django.contrib.auth.models import User

Locations=[('m','Mumbai'),
           ('p','Pune'),
           ('n','Nashik'),
           ('k','Kolhapur'),
            ('s','Sambhajinagar'),
            ('d','Dharashiv'),
           ('del','Delhi')]
class userform(forms.ModelForm):
    location=forms.ChoiceField(choices=Locations,widget=forms.Select())
    class Meta:
        model=Userinputmodel
        fields="__all__"
        widgets={
            'availiability':DateInput(attrs={'type':'date'}),

        }


    def clean_Total_sqft(self):
        total=self.cleaned_data['Total_sqft']
        if total<=300 or  total>=8000:
            raise forms.ValidationError("range for sqft is 301-7999")
        else:
            return total
    def clean_Bhk(self):
        flat=self.cleaned_data['Bhk']
        if flat>=15 & flat<=0.9:
            raise forms.ValidationError('FLat limit is upto 15')
        else:
            return flat




class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']