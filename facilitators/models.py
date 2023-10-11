from django.db import models
from django.contrib.auth.models import User
from student_inquiries.models import Post
from django.utils import timezone

class get_message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages')
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
    
class FacilitatorReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_facposts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_replies')
    reply = models.TextField(max_length=4000)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username     