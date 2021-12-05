from django.urls import path
from .views import login

app_name = 'markito'
urlpatterns = [
    path('', login, name="login")
]
