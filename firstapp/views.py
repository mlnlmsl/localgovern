from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

import pyrebase
config = {
  "apiKey": "AIzaSyAbLSZ6wFGRloWQQCka348uSZtZdojDqFw",
  "authDomain": "loca-9518f.firebaseapp.com",
  "databaseURL": "https://loca-9518f.firebaseio.com",
  "projectId": "loca-9518f",
  "storageBucket": "",
  "messagingSenderId": "1054814527011",
  "appId": "1:1054814527011:web:4ed004d9390b738e"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = db.child('')

# auth = firebase.auth()
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")

        else:
            messages.error(request, 'Invalid username or Password')
            return redirect('login')
    
    else:
        return render(request, 'pages/login.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')

def comparision(request):
    return render(request, 'pages/comparision.html')

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect( 'login')
    else:
        return render(request, 'pages/login.html')


