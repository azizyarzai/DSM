from django.shortcuts import render
from stamps.models import Category, Group

# Create your views here.


def home(request):
    categories = Category.objects.all()
    template = "pages/index.html"
    context = {
        "categories": categories,
    }
    return render(request, template, context)


def about(request):
    template = "pages/about.html"
    context = {}
    return render(request, template, context)
