from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from student_inquiries.models import Post


def home(request):
    return render(request, 'home.html')

def board(request):
    return render(request, 'board.html')



def post_request(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        Post.objects.create(message=message)
        return redirect('login')  # 'success' should be the name of your success URL pattern
    return HttpResponse("Invalid request method")  # Handle invalid request methods
