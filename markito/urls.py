from django.urls import path
from .views import home,products

app_name = 'markito'
urlpatterns = [
    path('', home, name="home"),
    path('products/',products,name="products"),
]
