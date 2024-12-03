from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.indexview,name='home'),
    path('products_list',views.list_products,name='list_product'),
    path('products_details',views.detail_product,name='detail_product'),


   

]

