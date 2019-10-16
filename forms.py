from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    login = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, max_length=10)