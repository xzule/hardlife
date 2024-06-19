from django.urls import path, include
from .views import signup
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('index.html', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='../index.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
]