from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userprofile(models.model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=500)
    image=models.ImageField(upload_to="user image")
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
