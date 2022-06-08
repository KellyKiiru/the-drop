from dataclasses import field
from django.forms import forms,ModelForm,TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        

class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=3300, required=True)
    class Meta:
        model = Comment
        fields = ["comment",]
        widgets = {
            'comment': TextInput(attrs={'class': 'input', 'placeholder': 'Write comment','style':'max-width:100%'})
        }