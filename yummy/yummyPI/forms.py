from django import  forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Categories


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32)
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=32)
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput())
    secret_word = forms.CharField(
        required=True,
        label='Secret_word',
        max_length=32)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'secret_word')


class CategoryRegistrationForm(forms.Form):
    category_name = forms.CharField(
        required=True,
        label='category Name',
        max_length=256)
    category_description = forms.CharField(
        required=True,
        label='category_description',
        max_length=256)

    class Meta:
        model = Categories
        fields = ('category_name', 'category_description')
