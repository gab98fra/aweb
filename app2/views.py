from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class DashboardView(TemplateView):

    template_name="app2.html"