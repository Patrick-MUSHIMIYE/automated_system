from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from student_inquiries.models import Post, Replie
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'home.html')

def board(request):
    return render(request, 'board.html')

def reply(request):
    return render(request, 'reply.html')

@login_required
def post_request(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user
        Post.objects.create(user=user, message=message)
        messages.info(request, 'successfully posted')
        return HttpResponse('Request successfully sent to an admin')  
    return HttpResponse("Invalid request method")

@login_required
def reply_to_post(request):
    if request.method == 'POST':
        msg = request.POST.get('reply')
        user = request.user
        post = Post.objects.get(id=1)
        # Create a new reply associated with the post
        Replie.objects.create(user=user, post=post, reply=msg)
        messages.info(request, 'Successfully replied to the post')
        return redirect('reply')

    return HttpResponse("Invalid request method")
