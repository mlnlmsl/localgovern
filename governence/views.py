# import pyrebase
# from django.shortcuts import render
# config = {
#     "apiKey": "AIzaSyAbLSZ6wFGRloWQQCka348uSZtZdojDqFw",
#     "authDomain": "loca-9518f.firebaseapp.com",
#     "databaseURL": "https://loca-9518f.firebaseio.com",
#     "projectId": "loca-9518f",
#     "storageBucket": "",
#     "messagingSenderId": "1054814527011",
#     "appId": "1:1054814527011:web:4ed004d9390b738e"
# }
# firebase = pyrebase.initialize_app(config)
# # auth = firebase.auth()

# # Get a reference to the database service
# db = firebase.database()


# def dashboard(request):
#     data = db.child('GovUpdate').get().val()
#     return render(request, 'dashboard.html', {'data': data})
