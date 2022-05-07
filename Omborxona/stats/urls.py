from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', StatsView.as_view(), name = 'stast'),
]