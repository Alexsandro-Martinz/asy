from django.contrib import admin
from django.urls import path

from backend import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('sobre', view=views.saiba_mais, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
