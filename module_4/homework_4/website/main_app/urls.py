from django.contrib import admin
from django.urls import path

from . import views

app_urls = [
    path("python_start", views.python_start, name="python_start"),

    path("python_basics/", views.python_basics, name="python_basics"),
    path("python_basics/conditional_statements", views.conditional_statements, name="conditional_statements"),
]

urlpatterns = [
    path("", views.index, name="index"),
    *app_urls
]
