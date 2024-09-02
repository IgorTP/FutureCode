from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/pages/index.html")


def python_start(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/pages/page_1.html")


def python_basics(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/pages/page_2.html")


def conditional_statements(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/pages/page_3.html")
