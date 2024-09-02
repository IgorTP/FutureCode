from django.urls import path

from . import views

urlpatterns = [
    path("", views.render_root, name="root"),
    path("pages/", views.render_main_pages, name="pages"),
    path("pages/page1", views.render_pg_1, name="page1"),
    path("pages/page2", views.render_pg_2, name="page2"),
    path("pages/page3", views.render_pg_3, name="page3"),
]
