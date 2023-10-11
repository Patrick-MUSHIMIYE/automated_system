from django.shortcuts import render, redirect
from django.http import HttpResponse
from facilitators.models import get_message
from .forms import RepliesForm
from student_inquiries.models import Post
from django.contrib.auth.decorators import login_required


def home2(request):
    return render(request, 'home2.html')

@login_required
def fac_post(request):
    if request.method == 'POST':
        get_msg = request.POST.get('message')
        user = request.user
        get_message.objects.create(user=user, message=get_msg)
        return HttpResponse("Request successfully sent to facilitator")
    return HttpResponse("Invalid request method")

# def reply_form(request):
#     form = RepliesForm(request.POST)
#     return render(request, 'reply.html', {form: form})

# # Create your views here.
# def post_reply(request):
#     if request.method == 'POST':
#         form = RepliesForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             reply_text = form.cleaned_data['message']  # Change this line
#             # Find the Post object based on the reply_text and user
#             post = Post.objects.get(message=reply_text, user=user)
#             # Create the get_message object with the related Post
#             get_message.objects.create(user=user, message=post, reply=reply_text)
#             return redirect('reply') 
#     return HttpResponse("Invalid request method")
    
            