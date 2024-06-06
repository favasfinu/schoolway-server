from django.shortcuts import render
from .serializers import UserprofileSerializer
from .models import Userprofile
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class UserprofileViewset(ModelViewSet):
    serializer_class=UserprofileSerializer
    queryset=Userprofile.objects.all()
