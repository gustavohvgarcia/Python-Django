from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("funcionarios/", views.funcionarios, name="funcionarios"),
    path("funcionarios/detalhes/<int:id>", views.detalhes, name="detalhes"),
    path("testing/", views.testing, name="testing"),
]
