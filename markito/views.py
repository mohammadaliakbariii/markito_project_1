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
from django.views.generic import TemplateView
from django_serverside_datatable.views import ServerSideDatatableView

# Create your views here.


class Home(TemplateView):
    template_name = "markito/home.html"





class ProductList(TemplateView):
    template_name = 'markito/products.html'





class ProductListView(ServerSideDatatableView):
    queryset = Products.objects.all()

    columns = ['image',
               'name',
               'category__name',
               'buy_price',
               'sell_price',
               'count',
               'side_costs',
               'is_active',
               ]


def dashboard(request):
    return render(request, 'markito/dashboard.html')



