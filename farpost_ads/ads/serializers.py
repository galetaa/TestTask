from rest_framework import serializers
from .models import Ad, Author
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'profile_link', 'city']


class AdSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Ad
        fields = ['title', 'ad_id', 'views_count', 'position', 'author']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
