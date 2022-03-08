from rest_framework import serializers
from userprofile.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name', 'email')