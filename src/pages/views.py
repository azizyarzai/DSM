from django.shortcuts import render
from stamps.models import Category, Group
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    template = "pages/index.html"
    return render(request, template)


def about(request):
    template = "pages/about.html"
    context = {}
    return render(request, template, context)


@login_required
def wish_list(request):
    template = 'orders/wish_list.html'
    context = {}
    return render(request, template, context)
