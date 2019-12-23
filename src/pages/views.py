from django.shortcuts import render

# Create your views here.


def home(request):
    template = "pages/index.html"
    context = {}
    return render(request, template, context)


def about(request):
    template = "pages/about.html"
    context = {}
    return render(request, template, context)
