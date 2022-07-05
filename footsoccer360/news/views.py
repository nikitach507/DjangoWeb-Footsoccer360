from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import *


def news_home(request):
    return render(request, 'main/index.html')