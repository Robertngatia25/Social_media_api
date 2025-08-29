from rest_framework import permissions, viewsets
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #Automatically link post to the logged-in user

