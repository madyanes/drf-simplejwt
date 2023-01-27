from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username # this username (in payload) will be `null`, because our custom user model.
        token['email'] = user.email
        return token
