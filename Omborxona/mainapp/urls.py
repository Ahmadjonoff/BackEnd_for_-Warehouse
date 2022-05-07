from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bolim/', Bolim.as_view(), name='bolim'),
    path('products/', ProductView.as_view(), name='product'),
    path('clients/', ClientView.as_view(), name='client'),
    path('logout/', Logout.as_view(), name='logout'),
    path('products/update/<int:son>/', ProductUpdate.as_view(), name='product-update'),
]