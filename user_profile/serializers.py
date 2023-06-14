
from rest_framework import serializers
from user_profile.models import  User


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'email', 'name', 'bio', 'profile_pic']
