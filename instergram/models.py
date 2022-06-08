from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pciture", null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} - Profile'
    
    def save(self):
        self.save()
        
def create_user_profile( instance, created,):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(instance):
    instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="static/", verbose_name="Picture")
    caption = models.CharField(max_length=500, verbose_name="Caption")
    posted = models.DateField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    comment_post = models.ForeignKey(Post,null=True,on_delete=models.SET_NULL,related_name="comment")
    comment_user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    comment = models.CharField(blank=False, max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.objects.get(id=id)
        comment.delete()

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
