from django.contrib import admin

# Register your models here.
from student_inquiries.models import Post, Replie

from .models import Post 
admin.site.register(Post)
admin.site.register(Replie)
