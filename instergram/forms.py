from django.forms import forms,ModelForm,TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from allauth.account.forms import SignupForm

# class UserSignUpForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class UserSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    bio = forms.CharField(max_length=255, label='Bio')
    def save(self, request):
        # create user the create profile
        user = super(UserSignUpForm, self).save(request)
        ### now save your profile 
        profile = Profile.objects.get_or_create(user=user)
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.bio = self.cleaned_data['bio']
        profile.save()
        return user

class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=3300, required=True)
    class Meta:
        model = Comment
        fields = ["comment",]
        widgets = {
            'comment': TextInput(attrs={'class': 'input', 'placeholder': 'Write comment','style':'max-width:100%'})
        }

class NewPostform(forms.ModelForm):    
    picture = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)

    class Meta:
        model = Post
        fields = ['picture', 'caption']
        
class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}), required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Location'}), required=True)

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'bio', 'location']
