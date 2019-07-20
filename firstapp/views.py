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
drinking_water = db.child('Municipality').child('Kathmandu').child('Wardno1').child('Problems').child('Drinking Water').shallow().get().val()
education = db.child('Municipality').child('Kathmandu').child('Wardno1').child('Problems').child('Education').shallow().get().val()
health = db.child('Municipality').child('Kathmandu').child('Wardno1').child('Problems').child('Health').shallow().get().val()
social_issues = db.child('Municipality').child('Kathmandu').child('Wardno1').child('Problems').child('Social Issues').shallow().get().val()
transperiancy = db.child('Municipality').child('Kathmandu').child('Wardno1').child('Problems').child('Transparency').shallow().get().val()

problem1 = []

for i in transperiancy:
    problem1.append(i)

problem1.sort(reverse=True)
num_transperiancy = len(problem1)

problem2 = []

for i in drinking_water:
    problem2.append(i)

problem2.sort(reverse=True)
num_drinking_water = len(problem2)

problem3 = []

for i in education:
    problem3.append(i)

problem3.sort(reverse=True)
num_education = len(problem3)

problem4 = []

for i in health:
    problem4.append(i)

problem4.sort(reverse=True)
num_health = len(problem4)

problem5 = []

for i in social_issues:
    problem5.append(i)

problem5.sort(reverse=True)
num_social_issues = len(problem5)

context = {
    "num_drinking_water" : num_drinking_water,
    "num_education" : num_education,
    "num_health" : num_health,
    "num_social_issues" : num_social_issues,
    "num_transperiancy" : num_transperiancy,
}


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
    return render(request, 'pages/dashboard.html', context)

def comparision(request):
    return render(request, 'pages/comparision.html')

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect( 'login')
    else:
        return render(request, 'pages/login.html')


