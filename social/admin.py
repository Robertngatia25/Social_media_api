from django.contrib import admin
from .models import Post, follower, Comment, Profile

admin.site.register(Post)
admin.site.register(follower)
admin.site.register(Comment)
admin.site.register(Profile)

# Register your models here.