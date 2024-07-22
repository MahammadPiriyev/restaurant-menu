from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories/<slug:category_slug>', views.category_detail, name="categorydetail")
]