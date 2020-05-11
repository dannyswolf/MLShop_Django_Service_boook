from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def login_page(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('Calendar/')

        else:
            messages.info(request, 'Λάθος όνομα χρήστη ή κωδικός')

    context = {}
    return render(request, "login/login.html", context)


def logout_page(request, *args, **kwargs):
    logout(request)
    return redirect('login:login')

