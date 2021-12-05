from django.urls import path
from .views import home

app_name = 'markito'
urlpatterns = [
    path('', home, name="home")
]
