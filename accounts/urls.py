from django.urls import path
from .views import login,log_out

app_name = 'accounts'
urlpatterns = [
    path('', login, name="login"),
    path('log_out/',log_out,name='log_out')
]
