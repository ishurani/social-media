from django.shortcuts import render
from . import models
from groups.models import Group
from django.views.generic import CreateView,DetailView,ListView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.

class Creategroup(CreateView):
    model=Group
    fields=('name','description')
    success_url=reverse_lazy('groups:all')

class Singlegroup(DetailView):
    model=Group

class Listgroup(ListView):
    model=Group
