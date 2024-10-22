from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from backend import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('sobre/', view=views.saiba_mais, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
