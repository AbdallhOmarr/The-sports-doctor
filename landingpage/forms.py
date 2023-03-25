from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trainer, Trainee
from django.db import transaction


class TrainerSignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        )
    )

    email = forms.EmailField(
        max_length=200,
        help_text="Required",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    dateofbirth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Date of Birth",
            }
        )
    )
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Mobile"}
        ),
    )
    national_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "National ID"}
        ),
    )
    account_type = forms.CharField(max_length=20, initial="Trainer")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "dateofbirth",
            "mobile",
            "national_id",
            "account_type",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        with transaction.atomic():
            user.save()
            trainer = Trainer(user=user, dateofbirth=self.cleaned_data["dateofbirth"])
            trainer.dateofbirth = self.cleaned_data["dateofbirth"]
            trainer.mobile = self.cleaned_data["mobile"]
            trainer.national_id = self.cleaned_data["national_id"]
            trainer.account_type = self.cleaned_data["account_type"]

            trainer.save()

        return user


class TraineeSignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        )
    )

    email = forms.EmailField(
        max_length=200,
        help_text="Required",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    dateofbirth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Date of Birth",
            }
        )
    )
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Mobile"}
        ),
    )
    account_type = forms.CharField(max_length=20, initial="Trainee")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "dateofbirth",
            "mobile",
            "account_type",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        with transaction.atomic():
            user.save()
            trainee = Trainee(user=user, dateofbirth=self.cleaned_data["dateofbirth"])
            trainee.dateofbirth = self.cleaned_data["dateofbirth"]
            trainee.mobile = self.cleaned_data["mobile"]
            trainee.account_type = self.cleaned_data["account_type"]

            trainee.save()

        return user

