from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products, Store
import json
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = "markito/home.html"


def json_info(request):
    products = Products.objects.filter(store__user=request.user)
    data = serialize('json',products)
    return HttpResponse(data,content_type="application/json")



@login_required
@csrf_exempt
def products(request):

<<<<<<< HEAD
=======
<<<<<<< HEAD
    products = Products.objects.filter(store__user=request.user)
=======
    if request.method=='POST':
        P

>>>>>>> 4bb4d318f18165a47ca236ffa7a8f6ad52449592

    return render(request, 'markito/products_1.html',context={
        "products":products,
    })
>>>>>>> parent of bc744c4 (send from ajax to view)

        return render(request,'markito/products_1.html')

def dashboard(request):
    return render(request, 'markito/dashboard.html')
