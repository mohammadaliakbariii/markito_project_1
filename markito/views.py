import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Products, Store
from django.views.generic import TemplateView
from django_serverside_datatable.views import ServerSideDatatableView
from django.http import JsonResponse, HttpResponse
from django_serverside_datatable import datatable
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import requests
# Create your views here.


class Home(TemplateView):
    template_name = "markito/home.html"


class ProductList(LoginRequiredMixin, TemplateView):
    template_name = 'markito/products.html'


class ProductListView(ServerSideDatatableView):

    def get(self, request, *args, **kwargs):
        queryset = Products.objects.filter(store__user=self.request.user)
        columns = ['image',
                   'name',
                   'category__name',
                   'buy_price',
                   'sell_price',
                   'count',
                   'side_costs',
                   'is_active',
                   'id',
                   ]
        self.queryset = queryset
        self.columns = columns
        result = datatable.DataTablesServer(request, self.columns, self.queryset).output_result()
        return JsonResponse(result, safe=False)



class Settings(LoginRequiredMixin, TemplateView):
    template_name = 'markito/settings.html'




class SettingsList(ServerSideDatatableView):
    def get(self, request, *args, **kwargs):
        queryset = Store.objects.filter(user=self.request.user)
        columns = [
                   'channel__name',
                   'name',
                   'created_date',
                    'updated',
                   ]
        self.queryset = queryset
        self.columns = columns
        result = datatable.DataTablesServer(request, self.columns, self.queryset).output_result()
        return JsonResponse(result, safe=False)



@csrf_exempt
def update_view(request,id):
    if request.method=='POST':
        new_name =request.POST.get("name")
        new_buy_price=request.POST.get('buy_price')
        new_sell_price=request.POST.get('sell_price')
        new_side_costs=request.POST.get('side_costs')
        new_count=request.POST.get('count')
        new_status=request.POST.get('is_active')
        product=Products.objects.filter(id=id)
        product=product.update(name=new_name,buy_price=new_buy_price,side_costs=new_side_costs,sell_price=new_sell_price,count=new_count,is_active=new_status)
        return HttpResponse(product)




@csrf_exempt
def delete_view(request,id):
    if request.method=='POST':
        product=Products.objects.filter(id=id)
        product.delete()
        return HttpResponse(product)



class AddChannel(TemplateView):
    template_name = 'markito/add_channel.html'



@csrf_exempt
def get_data(request):
        message=''
        url = "https://seller.digikala.com/api/v1/variants/"
        # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJ0b2tlbl9pZCI6NjIzMSwicGF5bG9hZCI6bnVsbH0.SRWCoiAumPyjtEKV2gKatWZw1IDUbcIqH9tj9oF-uOh_nTAkc6Bz9C7OEE5yp4fz'
        if request.method=="POST":
            token=request.POST['token']
            r = requests.get(url,headers={'Authorization': token})
            if r.status_code==200:

                record = r.json()

                print(record)

                return HttpResponse(record)

        else:
            return render(request,'markito/add_channel.html')

