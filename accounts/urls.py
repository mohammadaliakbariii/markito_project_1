from django.urls import path
from django.conf.urls import url
from .views import login,log_out,register,activate

app_name = 'accounts'
urlpatterns = [
    path('', login, name="login"),
    path('log_out/',log_out,name='log_out'),
    path('register/',register,name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),


]
