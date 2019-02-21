from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    profile = UserSerializer(source='authorId', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'authorId', 'title', 'body', 'created_at', 'profile')

