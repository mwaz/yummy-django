from django import  forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Categories


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'
        }),
        required=True,
        label='Username',
        max_length=32)
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Email'
        }),
        required=True,
        label='Email',
        max_length=32)
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput(attrs = { 'class':'form-control'} ))

    secret_word = forms.CharField(
        widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Secret Word'
        }),
        required=True,
        label='Secret_word',
        max_length=32)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'secret_word')


class CategoryRegistrationForm(forms.Form):
    category_name = forms.CharField(
        widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'category name'
        }),
        required=True,
        label='Category Name',
        max_length=256)

    category_description = forms.CharField(
         widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Category description'
        }),
        required=True,
        label='Category Description',
        max_length=256)

    class Meta:
        model = Categories
        fields = ('category_name', 'category_description')
