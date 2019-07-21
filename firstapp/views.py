from pyrebase import pyrebase
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse

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

auth = firebase.auth()


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
    data = db.child('users').get().val()
    print(data['Municipality'])
    return render(request, 'pages/dashboard.html', {'data': data})


def comparision(request):
    return render(request, 'pages/comparision.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return render(request, 'pages/login.html')


def issues_bar(request):
    return JsonResponse(format_wardwise_pie())


def issues_by_ward(request):
    return JsonResponse(format_pie_data())


def format_pie_data():
    data = {}
    legend_data = ['Ward 1', 'Ward 2']
    series_data = [{'value': 200, 'name': 'Ward 1'},
                   {'value': 200, 'name': 'Ward 2'}]
    data['title'] =  {'text': 'Issues by Ward', 'x': 'center'}
    data['tooltip'] = {'trigger': 'Issues',
                        'formatter': '{a} <br/>{b} : {c} ({d}%)'}

    data['legend'] = {'orient':'vertical','left': 'left','data':legend_data}
    data['series'] = [{'name': 'series', 'type': 'pie',
                        'radius': '55%', 'cemter': '["50%","60%"]', 'data': series_data}]
    data['itemStyle'] = {'emphasis': {'shadowBlur': 10,
                                       'shadowOffsetX': 0, 'shadowColor': 'rgba(0, 0, 0, 0.5)'}}

    # data = {'legend_data': legend_data, 'series_data': series_data}
    return data


def format_wardwise_pie():
    data = {}
    legend_data = ['Construction', 'Socail Issues',
                   'Education', 'Drinking Water', 'Sanitation']
    series_data = [{'value': 200, 'name': 'Construction'},
                   {'value': 200, 'name': 'Socail Issues'},
                   {'value': 200, 'name': 'Education'},
                   {'value': 200, 'name': 'Drinking Water'},
                   {'value': 200, 'name': 'Sanitation'}]
    data['title'] = {'text': 'Issues by Category', 'x': 'center'}
    data['tooltip'] = {'trigger': 'Issues',
                       'formatter': '{a} <br/>{b} : {c} ({d}%)'}

    data['legend'] = {'orient': 'vertical',
                      'left': 'left', 'data': legend_data}
    data['series'] = [{'name': 'Issues', 'type': 'pie',
                       'radius': '55%', 'cemter': '["50%","60%"]', 'data': series_data}]
    data['itemStyle'] = {'emphasis': {'shadowBlur': 10,
                                      'shadowOffsetX': 0, 'shadowColor': 'rgba(0, 0, 0, 0.5)'}}
    return data
