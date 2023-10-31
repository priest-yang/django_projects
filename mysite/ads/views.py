from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ads.models import Ad
from ads.forms import AdForm
from ads.owner import *

class AdCreateView(OwnerCreateView):
    model = Ad
    fields =  ["title", "text", "price"]

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields =  ["title", "text", "owner", "price"]

class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields =  ["title", "text"]  #'__all__'
    # success_url = reverse_lazy('ads:all')

class AdListView(OwnerListView):
    model = Ad
    fields =  ["title", "text", "price"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdDetailView(OwnerDetailView):
    model = Ad
    fields =  ["title", "text", "price"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context