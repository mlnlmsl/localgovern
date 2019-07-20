from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signout/', views.signout, name='signout'),
    path('comparision/', views.comparision, name='comparision'),
    path('get_issues', views.issues_bar),
    path('issues_by_ward', views.issues_by_ward),
    # path('ward_compare')
]
