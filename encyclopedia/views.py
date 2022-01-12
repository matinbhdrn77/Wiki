from typing_extensions import Self
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from markdown_deux import markdown

from . import util


class IndexView(TemplateView):
    template_name = "encyclopedia/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = util.list_entries()
        return context


class EntryPageViw(View):
    def get(self, request, title):
        entry = util.get_entry(title) #str
        return render(request, "encyclopedia/entry-page.html", {
            "entry":markdown(entry),
            "title":title
        })
        
        