from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products, Store
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'markito/home.html')


@login_required
def products(request):
    products = Products.objects.filter(store__user=request.user)
    p = Paginator(products, 10)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    context = {
        "list_products": products_list,

    }
    return render(request, 'markito/products.html', context)


def dashboard(request):
    return render(request, 'markito/dashboard.html')
