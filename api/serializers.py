#api/serializers.py

from rest_framework import serializers
from accounts import models

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        fields = ('username','password','email')
        model = models.User

class UserProfileInfoSerializer(serializers.ModelSerializer):
     class Meta():
         fields = ('id','name','phone')
         model = models.UserProfileInfo
