from django.urls import path

from .views import Home,ProductListView,ProductList,Settings,SettingsList,update_view

app_name = 'markito'
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('data/', ProductListView.as_view()),
    path('products/', ProductList.as_view(), name='products_records'),
    path('settings/',Settings.as_view(),name='settings'),
    path('info/',SettingsList.as_view(),name='info'),
    path("update/<int:id>/",update_view,name='update_view')

]