from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "author", "content", "media", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]
