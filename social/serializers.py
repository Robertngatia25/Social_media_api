from rest_framework import serializers
from .models import Profile, Post, Comment, follower
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]    

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        field = ["id", "user","bio","location", "profile_pic",]

class Postserializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class meta:
        model = Post
        fields = ["id", "author", "content", "created_at","updated_at","media"]

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = Postserializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "post", "content"]

class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)
    class Meta:
        model = follower
        fields = ["id", "user", "follower", "following"]