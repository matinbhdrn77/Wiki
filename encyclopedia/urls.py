from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("wiki/<str:title>", views.EntryPageViw.as_view(), name="entry-page")
]
