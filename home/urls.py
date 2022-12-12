from django.urls import path
from home.views import home
from .views import *

urlpattens = [
    path('', home),
]
