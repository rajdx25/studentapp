from logging import PlaceHolder
from django import forms



class Form_view(forms.Form):
    studentname=forms.CharField(widget=forms.TextInput(attrs={'PlaceHolder':'enter your name','class':'form_control'}))              
    studentaddress =forms.CharField(widget=forms.Textarea())
    studentnumber=forms.CharField(widget=forms.NumberInput())
    studentemail=forms.EmailField()
    


    