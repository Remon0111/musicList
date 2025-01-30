"""
URL configuration for searchMusic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from search_app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("opening/", views.opening, name="opening"),
    path("mainpage/", views.mainpage, name="main"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='account_system/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account_system/logout.html'), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path("detail/<int:pk>/", views.detail.as_view(), name="detail"),
    path("update/<int:pk>", views.update.as_view(), name="update"),
    path('edit/', views.edit.as_view(), name="edit"),
    path('delete/<int:pk>', views.delete.as_view(), name="delete"),
    path('Jpop/', views.Jpop, name="Jpop"),
    path('bokaro/', views.bokaro, name="bokaro"),
    path('rock/', views.rock, name="rock"),
    path('hiphop/', views.hiphop, name="hiphop"),
    path('jaz/', views.jaz, name="jaz"),
    path('classic/', views.classic, name="classic"),
    path('youtube/', views.youtubeurl, name='youtube'),
    path("spotify/", views.spotifyurl, name='spotify'),
    path('error/', views.errorpage, name="error"),
]