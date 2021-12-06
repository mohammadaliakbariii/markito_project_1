from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'markito/home.html')


def products(request):
    return render(request,'markito/products.html')



def dashboard(request):
    return render(request,'markito/dashboard.html')






