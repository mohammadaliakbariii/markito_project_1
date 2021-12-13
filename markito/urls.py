from django.urls import path

from .views import Home,ProductListView,ProductList,Settings,SettingsList,update_view,delete_view,AddChannel,get_data

app_name = 'markito'
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('data/', ProductListView.as_view()),
    path('products/', ProductList.as_view(), name='products_records'),
    path('settings/',Settings.as_view(),name='settings'),
    path('info/',SettingsList.as_view(),name='info'),
    path("update/<int:id>/",update_view,name='update_view'),
    path('delete/<int:id>/',delete_view,name='delete_view'),
    path('add_channel/',AddChannel.as_view(),name="add_channel"),
    path('get_data/',get_data,name="get_data")
]