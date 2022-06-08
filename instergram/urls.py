from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.homepage,name='homepage'),
    path('signup',views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LoginView.as_view(),name='logout'),
]