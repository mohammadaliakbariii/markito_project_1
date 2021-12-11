from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Products
from django.views.generic import TemplateView
from django_serverside_datatable.views import ServerSideDatatableView
from django.http import JsonResponse
from django_serverside_datatable import datatable


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
                   ]
        self.queryset = queryset
        self.columns = columns
        result = datatable.DataTablesServer(request, self.columns, self.queryset).output_result()
        return JsonResponse(result, safe=False)


def dashboard(request):
    return render(request, 'markito/dashboard.html')
