from django import forms
from django.contrib.auth import password_validation


class UserLoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)