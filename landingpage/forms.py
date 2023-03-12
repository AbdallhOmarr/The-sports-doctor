from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserCreateForm(UserCreationForm):
    selection = (
        ('1', 'Male'),
        ('2', 'Female')
    )
    gender = forms.ChoiceField(required=True, choices=selection, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        label='Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "gender", "password1", "password2", "first_name", "last_name", "nationality", "address", "city", "birth_date", "weight", "height")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.gender = self.cleaned_data["gender"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.nationality = self.cleaned_data["nationality"]
        user.address = self.cleaned_data["address"]
        user.city = self.cleaned_data["city"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.weight = self.cleaned_data["weight"]
        user.height = self.cleaned_data["height"]

        if commit:
            user.save()
        return user
