from rest_framework import permissions, viewsets, status
from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from notifications.models import Notification
from accounts.models import Follow
from django.db.models import Q

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #Automatically link post to the logged-in user
    #Feeds endpoints
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feeds(self, request):
        # Get the IDs of users that the current user is following.
        following_ids = Follow.objects.filter(
            follower=request.user
        ).values_list('following_id', flat=True)

        # Create a queryset for posts from followed users and the user's own posts.
        posts = Post.objects.filter(
            Q(author_id__in=following_ids) | Q(author=request.user)
        ).distinct().order_by("-created_at")

        # Pagination
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    # Like Toggle
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        try:
            # If like exists, delete it (unlike)
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            # If like does not exist, create it (like)
            Like.objects.create(user=request.user, post=post)
            if post.author != request.user:  # Don't notify self
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post,
                )
            return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)




    # Nested comments
    @action(detail=True, methods=['get', 'post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def comments(self, request, pk=None):
        post = self.get_object()

        if request.method == "GET":
            comments = post.comments.all().order_by("-created_at")
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == "POST":
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                new_comment = serializer.save(author=request.user, post=post)

                if post.author != request.user:  # Don't notify self
                    Notification.objects.create(
                        recipient=post.author,
                        actor=request.user,
                        verb="commented on your post",
                        target=new_comment,  # Assign the new comment object directly
                    )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)