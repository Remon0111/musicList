from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


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
    path('youtube/', views.youtubeurl, name='youtube'),
    path("spotify/", views.spotifyurl, name='spotify'),
    path('error/', views.errorpage, name="error"),
]