from django.urls import path

from .views import Home,ProductListView,ProductList

app_name = 'markito'
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('data/', ProductListView.as_view()),
    path('products/', ProductList.as_view(), name='products_records'),




]