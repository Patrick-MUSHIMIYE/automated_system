from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    message = models.TextField(max_length=4000, unique=True)
