from  djoser.serializers import  UserCreateSerializer
from  rest_framework_simplejwt.serializers import  TokenObtainPairSerializer
from  django.contrib.auth import get_user_model
from rest_framework import serializers
from django.conf import settings
user = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
          class Meta(UserCreateSerializer):
                    model = user
                    fields = ['id', 'email', 'name', 'password']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
          @classmethod
          def  get_token(cls, user):
              token =  super().get_token(user)
              token['name'] = user.name
              token['email'] = user.email
              return  token

class UserProfileSerializer(serializers.ModelSerializer):
    followers_name = serializers.StringRelatedField(source='followers.username',many=False)
    class Meta:
         model = user
         fields = ['id', 'email', 'name', 'username', 'followers', 'followers_name']