from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products,Store
# Create your views here.

def home(request):
    return render(request,'markito/home.html')

@login_required
def products(request):
    store = Store.objects.filter(user=request.user)
    products = Products.objects.filter(store=store)
    context = {
        'products':products,
    }
    return render(request,'markito/products.html',context)



def dashboard(request):
    return render(request,'markito/dashboard.html')






