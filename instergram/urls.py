from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import static

urlpatterns= [
    path('',views.homepage,name='homepage'),
    path('signup',views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LoginView.as_view(),name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)