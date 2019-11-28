#api/serializers.py

from rest_framework import serializers
from accounts import models

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        fields = ('username','password')
        model = models.User

class UserProfileInfoSerializer(serializers.ModelSerializer):
     class Meta():
         fields = ('id','name','phone','email')
         model = models.UserProfileInfo
