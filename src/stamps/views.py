from django.shortcuts import render

# Create your views here.


def browse_stamps(request):
    template = "stamps/browse_stamps.html"
    context = {}
    return render(request, template, context)
