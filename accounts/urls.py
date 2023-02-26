from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView
from knox import views as knox_views
from .views import LoginAPI


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
