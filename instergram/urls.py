from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('',views.homepage,name='homepage'),
    # path('signup',views.signup,name='sign-up'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('newpost', views.newpost, name='newpost'),
    path('<post_id>/like', views.like, name='like'),
    path('accounts/<int:id>/', views.userprofile, name='profile'),
    path('profile/edit', views.editprofile, name="editprofile"),
    #path('sign-in/', auth_views.LoginView.as_view(template_name="registration/sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('logout/',auth_views.LoginView.as_view(),{"next_page": '/'},name='logout'),
    path('<username>/follow/<option>/', follow, name='follow'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)