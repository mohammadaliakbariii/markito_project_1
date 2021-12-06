from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser

from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.

def register(request):
    message = ''
    if request.method == "POST":
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        full_name = request.POST['full_name']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if CustomUser.objects.filter(email=email) or CustomUser.objects.filter(phone_number=phone_number):
            message = 'this username or email is already exit please choose another please'
            return render(request, 'accounts/register.html', context={'message': message})

        if password != password2:
            message = 'passwords are not match!!!'
            return render(request, 'accounts/register.html', context={'message': message})

        newuser = CustomUser.objects.create_user(email=email, phone_number=phone_number, full_name=full_name,
                                                 password=password)
        newuser.full_name = full_name
        newuser.save()
        message = 'signUp successfully!!!please logIN'
        return redirect('markito:home')
    else:
        return render(request, 'accounts/register.html', context={"message": message})


def login(request):
    message = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            # return render(request, 'markito/home.html')
        else:
            message = 'your email or password is wrong!!!'

    return redirect('/')


def log_out(request):
    logout(request)
    return redirect("markito:home")
