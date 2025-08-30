from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    media = models.FileField(upload_to='post_media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    

class Like(models.Model):
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Ensure a user can't like the same post twice.
        """
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"