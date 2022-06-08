from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login

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
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_profile=Profile(
                user=new_user,
                name=username
            )
            user_profile.save_profile()
            
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],)
            login(request, new_user)
            # return redirect('editprofile')
            return redirect('homepage')
    elif request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = UserSignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'all-pages/registration_form.html', context)

def signin(request):
    pass
def logout(request):
    pass