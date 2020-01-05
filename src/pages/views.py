from django.shortcuts import render
from stamps.models import Category, Group

# Create your views here.


def home(request):
    template = "pages/index.html"
    return render(request, template)


def about(request):
    template = "pages/about.html"
    context = {}
    return render(request, template, context)
