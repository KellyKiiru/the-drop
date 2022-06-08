from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    user= request.user
    all_users = User.objects.all()
    profile = Profile.objects.all()
    post = Post.objects.all()
    title = 'Welcome to instagram'
        
    context = {
        'post': post,
        'profile': profile,
        'all_users': all_users,
        'title':title
    }
    return render(request,'all-pages/homepage.html', context=context)
def signup(request):
    pass
def signin(request):
    pass
def logout(request):
    pass