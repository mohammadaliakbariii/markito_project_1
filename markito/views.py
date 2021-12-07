from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products, Store
import json
from django.http import HttpResponse
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'markito/home.html')



def json_info(request):
    products = Products.objects.filter(store__user=request.user)
    data = serialize('json',products)
    return HttpResponse(data,content_type='application/json')



@login_required
def products(request):
    pass
    products = Products.objects.filter(store__user=request.user)

    return render(request, 'markito/products_1.html',context={
        "products":products,
    })


def dashboard(request):
    return render(request, 'markito/dashboard.html')
