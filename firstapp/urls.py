from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signout/', views.signout, name='signout'),
    path('comparision/', views.comparision, name='comparision'),
]