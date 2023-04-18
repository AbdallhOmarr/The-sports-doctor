from django.db import models
from django.contrib.auth.models import User


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, default="trainer")
    dateofbirth = models.DateField()
    mobile = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Trainee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, default="trainee")
    dateofbirth = models.DateField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    long_text = models.CharField(max_length=200)
    img = models.ImageField()
    # url = models.CharField(max_length=200)

