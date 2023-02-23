from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass

