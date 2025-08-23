from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to='post_media/', blank=True, null=True) # optional field when creating a post

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at[:30]}"
class Profile(models.Model):
    """
    Profile extend to all users,
    each user shall have a profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
 
    def __str__(self):
        return f"{self.user.username}'s Profile"

class follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers') # people following the user
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following') # people the user follows 
    created_at = models.DateTimeField(auto_now_add=True)
    class meta:
        unique_together = ('user', 'follower')
        
    def __str__(self):
        return f"{self.follower.username} follows {self.follower.username}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"

