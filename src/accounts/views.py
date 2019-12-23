from django.shortcuts import render

# Create your views here.


def login(request):
    template = "accounts/login.html"
    context = {}
    return render(request, template, context)


def register(request):
    template = "accounts/register.html"
    context = {}
    return render(request, template, context)
