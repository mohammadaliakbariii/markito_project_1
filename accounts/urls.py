from django.urls import path
from django.conf.urls import url
from .views import login,log_out,register

app_name = 'accounts'
urlpatterns = [
    path('', login, name="login"),
    path('log_out/',log_out,name='log_out'),
    path('register/',register,name="register"),


]
