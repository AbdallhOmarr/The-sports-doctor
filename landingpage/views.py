from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@csrf_exempt
def home(request):
    context = {}
    return render(request, "index.html", context)


@csrf_exempt
def loginView(request):
    print("login ")
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Password is incorrect")

    context = {"key": "login"}
    return render(request, "login_register.html", context)


@csrf_exempt
def logoutView(request):
    print("logout")
    logout(request)
    return redirect("/")


@csrf_exempt
def register(request):
    trainee_form = forms.TraineeSignupForm()
    trainer_form = forms.TrainerSignupForm()
    context = {
        "trainee_form": trainee_form,
        "trainer_form": trainer_form,
        "key": "register",
    }

    if request.method == "POST" and request.POST.get("account_type") == "trainee":
        trainee_form = forms.TraineeSignupForm(request.POST)
        if trainee_form.is_valid():
            user = trainee_form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            context = {
                "trainee_form": trainee_form,
                "trainer_form": trainer_form,
                "key": "register",
            }
            return render(request, "index.html", context)
        else:
            for field, errors in trainee_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            print("trainer form is not valid")
            context = {
                "trainee_form": trainee_form,
                "trainer_form": trainer_form,
                "key": "register",
            }

            return trainee_signup(request)

    elif request.method == "POST" and request.POST.get("account_type") == "trainer":
        trainer_form = forms.TrainerSignupForm(request.POST)
        if trainer_form.is_valid():
            user = trainer_form.save(commit=False)
            user.save()
            print("trainer saved")
            login(request, user)
            context = {
                "trainee_form": trainee_form,
                "trainer_form": trainer_form,
                "key": "register",
            }
            return render(request, "index.html", context)
        else:
            for field, errors in trainer_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            print("trainer form is not valid")
            context = {
                "trainee_form": trainee_form,
                "trainer_form": trainer_form,
                "key": "register",
            }

            return trainer_signup(request)


@csrf_exempt
def select_user_type(request):
    context = {}
    return render(request, "userselection.html", context)


@csrf_exempt
def trainee_signup(request):
    form = forms.TraineeSignupForm()
    context = {"form": form, "key": "register"}

    print("trainee ")
    return render(request, "trainee_signup.html", context)


@csrf_exempt
def trainer_signup(request):
    form = forms.TrainerSignupForm()
    context = {"form": form, "key": "register"}
    print("trainer ")
    return render(request, "trainer_signup.html", context)


@csrf_exempt
@login_required
def profile(request):
    context = {}
    # pass user info form
    username = request.user
    user = models.User.objects.filter(username=username)
    if request.user.groups.filter(name="Trainer").exists():
        # Do something if the user is a Trainer
        return render(request, "trainer_profile.html", context)
    elif request.user.groups.filter(name="Trainee").exists():
        # Do something if the user is a Trainee
        return render(request, "trainee_profile.html", context)
    elif request.user.groups.filter(name="admin").exists():
        print("admin")
        # Do something else if the user is not a Trainer or Trainee
        return render(request, "admin_profile.html", context)
    print("here's my profile")
    print(request.user.groups.filter(name="admin"))


@receiver(post_save, sender=models.Trainer)
def add_trainer_to_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name="Trainer")
        group = Group.objects.get(name="Trainer")

        instance.user.groups.add(group)


@receiver(post_save, sender=models.Trainee)
def add_trainee_to_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name="Trainee")
        group = Group.objects.get(name="Trainee")
        instance.user.groups.add(group)


def service_details(request):
    context = {}
    return render(request, "service-details.html", context)


def service_details2(request):
    context = {}
    return render(request, "service-details-2.html", context)


def service_details3(request):
    context = {}
    return render(request, "service-details-3.html", context)


def service_details4(request):
    context = {}
    return render(request, "service-details-4.html", context)


def service_details5(request):
    context = {}
    return render(request, "service-details-5.html", context)


def service_details6(request):
    context = {}
    return render(request, "service-details-6.html", context)


def educational_materials(request):
    context = {}
    return render(request, "education_materials.html", context)


def fellowships(request):
    context = {}
    return render(request, "fellowships.html", context)


def services(request):
    context = {}
    return render(request, "services.html", context)


def blog(request):
    context = {}
    return render(request, "blog.html", context)
