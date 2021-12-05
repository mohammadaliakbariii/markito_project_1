from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.


def login(request):
    message = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request,user)
            return render(request,'markito/home.html')
        else:
            message = 'your email or password is wrong!!!'



    return render(request,'accounts/login.html',context={
        'message':message,
    })


def log_out(request):
    logout(request)
    return redirect("markito:home")



