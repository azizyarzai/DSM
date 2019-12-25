from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.


def login(request):
    if request.method == 'POST':
        # Login User
        email = request.POST.get('email_phone')
        password = request.POST.get('pass')

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            if user.profile.blocked:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
            else:
                messages.error(
                    request, 'Your account has been blocked.')
                return HttpResponseRedirect(reverse_lazy('accounts:login'))
        else:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(reverse_lazy('accounts:login'))
    else:
        return render(request, 'accounts/login.html')


def register(request):
    template = "accounts/register.html"
    context = {}
    return render(request, template, context)


def dashboard(request):
    template = "accounts/dashboard.html"
    context = {}
    return render(request, template, context)
