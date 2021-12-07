from django.urls import path
from .views import home,products,json_info

app_name = 'markito'
urlpatterns = [
    path('', home, name="home"),
    path('products/',products,name="products"),
    path('info/',json_info,name="json_info"),
]
