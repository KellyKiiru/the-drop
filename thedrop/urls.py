from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('nadsk/fen/', TemplateView.as_view(template_name='all-pages/first.html')),
    path('admin/', admin.site.urls),
    path('',include('instergram.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('login/', LoginView.as_view(),name='login'),
    # path('login/', auth_views.LoginView.as_view(),name='login'),
    # path('accounts/',include('registration.backends.simple.urls')),
]
