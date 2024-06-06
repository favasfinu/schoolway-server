from rest_framework import serializers
from .models import Userprofile,Posting



class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userprofile
        field="__all__"
        read_only=["date"]