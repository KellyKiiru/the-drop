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
        
    
class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="static/", verbose_name="Picture")
    caption = models.CharField(max_length=500, verbose_name="Caption")
    posted = models.DateField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)