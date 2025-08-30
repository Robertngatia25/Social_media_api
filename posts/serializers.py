from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "content", "title", "media", "created_at", "updated_at", "comments", "likes_count"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def get_comments(self, obj):
        """
        Serializes the first 10 comments for a given post.
        """
        comments = obj.comments.all()[:10].order_by("-created_at")  # limit to 10 comments for performance
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at', 'post']