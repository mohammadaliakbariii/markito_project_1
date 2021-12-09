from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_serverside_datatable.views import ServerSideDatatableView

from .models import Products, Store
import json
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import TemplateView


# Create your views here.


class Home(TemplateView):
    template_name = "markito/home.html"


# def json_info(request):
#     products = Products.objects.filter(store__user=request.user)
#     data = serialize('json', products)
#     return HttpResponse(data, content_type="application/json")




class ItemListView(ServerSideDatatableView):
    queryset = Products.objects.all()
    columns = ['image', 'name', 'count']



# @login_required
@csrf_exempt
def products(request):
    # return render(request, 'markito/products.html')
    return render(request,'markito/PRODUCTS_1.html')

def dashboard(request):
    return render(request, 'markito/dashboard.html')


class ItemListView(ServerSideDatatableView):
    queryset = Products.objects.all()
    columns = ['field.image', 'fields.name', 'fields.count']
