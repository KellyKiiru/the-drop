from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
# @login_required
def homepage(request):
    user= request.user
    all_users = User.objects.all()
    profile = Profile.objects.all()
    post = Post.objects.all()
    title = 'Instagram'

    context = {
        'post': post,
        'profile': profile,
        'all_users': all_users,
        'title':title,
        'user':user,
    }
    return render(request,'all-pages/homepage.html', context=context)

# def signup(request):
#     #form = UserSignUpForm()
#     if request.method == "POST":
#         form = UserSignUpForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
            
#             user_profile=Profile(
#                 user=new_user,
#             )
#             #user_profile.save_profile()
            
#             new_user = authenticate(username=form.cleaned_data['username'],
#                                     password=form.cleaned_data['password1'],)
#             login(request, new_user)
#             return redirect('homepage')
#     elif request.user.is_authenticated:
#         return redirect('homepage')
#     else:
#         form = UserSignUpForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'registration/registration_form.html', context=context)


# @login_required
def userprofile(request,id):
    user_name = User.objects.get(id=id)
    user_profile = Profile.objects.get(user_profiler_id = id.id)
    user_posts = Post.objects.filter(user=user_name.id)
    following_count = Follow.objects.filter(follower=user_name.id).count()
    posts_count = Post.objects.filter(user=user_profile).count()
    post_comments = Comment.objects.all()

    comment_form = NewCommentForm()
    user_name_title = user_name
    title = f"{user_name_title}'s Profile"

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            comment_post_id = request.POST.get('comment_post')

            user = request.user
            user_profile = Profile.objects.get(user=user.id)
            comment_post = Post.objects.get(id=comment_post_id)
            user_comment = comment_form.cleaned_data['comment']

            comment = Comment(
                user=user,
                user_profile=user_profile,
                user_comment=user_comment,
                comment_post=comment_post
                )
            comment.save()
            return redirect('homepage')
    
    context={
        'user_name':user_name,
        'comment_form':comment_form,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'post_comments':post_comments,
        'title':title,
        'posts_count':posts_count,
        'following_count':following_count,
    }
    return render(request,'all-pages/profile.html',context=context)


# @login_required
def newpost(request):
    form = NewPostform(request.POST, request.FILES)
    
    if request.method == "POST":
        user = request.user
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            profile = get_object_or_404(Profile, user_profiler=user)
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            user = Profile.objects.get(user_profiler=user.id)
            new_post = Post(
                picture = picture,
                caption = caption,
                user=user,
            )
            new_post.save()
            return redirect('homepage')
    else:
        form = NewPostform()
    context = {
        'form': form
    }
    return render(request, 'all-pages/newpost.html', context=context)

# @login_required(login_url='login/')
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.likes = current_likes
    post.save()
    return redirect('homepage')

def editprofile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('homepage', profile.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'all-pages/editprofile.html',context=context)


def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
        return HttpResponseRedirect(reverse('homepage'))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('homepage'))

