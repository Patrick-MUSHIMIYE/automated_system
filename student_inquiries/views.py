from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from student_inquiries.models import Post
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def board(request):
    return render(request, 'board.html')

def post_request(request):
    if request.method == 'POST':
        message = request.POST.get('message', 'created_at')
        user = request.user
        Post.objects.create(user=user, message=message)
        messages.info(request, 'successfully posted')
        return redirect('home')  
    return HttpResponse("Invalid request method")
