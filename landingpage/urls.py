"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),  # type: ignore
    path("accounttype", views.select_user_type, name="user_selection_type"),
    path("trainer_signup", views.trainer_signup, name="trainer_signup"),
    path("trainee_signup", views.trainee_signup, name="trainee_signup"),
    path("profile", views.profile, name="profile"),  # type: ignore
    path("services", views.services, name="services"),
    path("service-details", views.service_details, name="service-detail"),
    path("service-details-2", views.service_details2, name="service-detail-2"),
    path("service-details-3", views.service_details3, name="service-detail-3"),
    path("service-details-4", views.service_details4, name="service-detail-4"),
    path("service-details-5", views.service_details5, name="service-detail-5"),
    path("service-details-6", views.service_details6, name="service-detail-6"),
    path(
        "educational-materials",
        views.educational_materials,
        name="educational-materials",
    ),
    path("fellowships", views.fellowships, name="fellowships"),
    path("blog", views.blog, name="blog"),
    path("blog-details", views.blog_details, name="blog-details"),
]
