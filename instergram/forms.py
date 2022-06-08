from dataclasses import field
from django.forms import forms
from django.contrib.auth.models import User


class UserSignUpForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','email','password']