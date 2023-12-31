from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
    
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    reply = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username