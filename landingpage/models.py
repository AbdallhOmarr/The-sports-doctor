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
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    dateofbirth = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
