from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signup')
def homepage(request):
    return HttpResponse("Hello World")
def signup(request):
    pass
def signin(request):
    pass
def logout(request):
    pass