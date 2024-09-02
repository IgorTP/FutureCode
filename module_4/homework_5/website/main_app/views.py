from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def render_root(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/root.html")


def render_main_pages(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/main_pages.html")


def render_pg_1(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_1.html")


def render_pg_2(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_2.html")


def render_pg_3(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_3.html")
