from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("wiki/<str:title>", views.EntryPageViw.as_view(), name="entry-page"),
    path("search-result/", views.SearchView.as_view(), name="search"),
    path("create-page/", views.CreateView.as_view(), name="create-page"),
    path("edite-page/<str:title>", views.EditePageView.as_view(), name="edite-page"),
    path("random/", views.RandomPageView.as_view(), name="random-page")
]
