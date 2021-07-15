from django import forms 
from django.forms import widgets


class LoginForm(forms.Form):
    username = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)