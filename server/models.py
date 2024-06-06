from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Userprofile(models.Model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=500)
    image=models.ImageField(upload_to="user image")
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Posting(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="posting_image")

    caption=models.CharField(max_length=500)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
