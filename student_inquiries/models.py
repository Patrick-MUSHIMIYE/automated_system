from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.TextField(max_length=4000, unique=True)
    
    def __str__(self):
        return self.message