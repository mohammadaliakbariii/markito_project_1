from django.urls import path

from .views import Home,products,json_info

app_name = 'markito'
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('products/',products,name="products"),
    path('info/',json_info,name="json_info"),


]
