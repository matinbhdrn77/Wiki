import re
from typing_extensions import Self
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from markdown_deux import markdown
from django.urls import reverse

from . import util


class IndexView(TemplateView):
    template_name = "encyclopedia/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = util.list_entries()
        return context


class EntryPageViw(View):
    def get(self, request, title):
        entry = util.get_entry(title)  # str
        if entry == None:
            entry = "# This encyclopedia doesn't exist"
        return render(request, "encyclopedia/entry-page.html", {
            "entry": markdown(entry),
            "title": title
        })


class SearchView(View):
    def post(self, request):
        search_input = request.POST["q"].lower()
        
        if search_input in util.list_entries():
            return HttpResponseRedirect(reverse("entry-page", args=[search_input]))

        same_entries = []
        for entry in util.list_entries():
            if search_input in entry.lower():
                same_entries.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries": same_entries,
        })
