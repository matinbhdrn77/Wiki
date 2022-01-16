import re
from turtle import title
from typing_extensions import Self
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import FormView
from markdown_deux import markdown
from django.urls import reverse
import random

from . import util
from .forms import CreatePageForm


class IndexView(TemplateView):
    template_name = "encyclopedia/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = util.list_entries()
        return context


class EntryPageViw(TemplateView):
    template_name = "encyclopedia/entry-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs["title"]
        print(title)
        entry = util.get_entry(title)  # str
        if entry == None:
            entry = "# This encyclopedia doesn't exist"
        context["entry"] = markdown(entry)
        context["title"] = title
        return context


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


class CreateView(FormView):
    template_name = 'encyclopedia/create-page.html'
    form_class = CreatePageForm

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        content = form.cleaned_data["contentMd"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry-page", args=[title]))


class EditePageView(TemplateView):
    template_name = "encyclopedia/create-page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs["title"]
        content = util.get_entry(title)
        form = CreatePageForm(initial={"contentMd":content, "title":title})
        context["title"] = title
        context["form"] = form
        context["edite"] = True
        return context


class RandomPageView(View):
    def get(self, request):
        entry_list = util.list_entries()
        entry_title = random.choice(entry_list)
        return HttpResponseRedirect(reverse("entry-page", args=[entry_title]))