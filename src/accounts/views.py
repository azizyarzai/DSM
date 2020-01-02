from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import urllib.request
import urllib.parse
import json
from django.conf import settings
from .models import Profile
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
    else:
        if request.method == 'POST':
            # Login User
            email = request.POST.get('email_phone')
            password = request.POST.get('pass')

            user = auth.authenticate(username=email, password=password)

            if user is not None:
                if user.profile.blocked:
                    messages.error(
                        request, 'Your account has been blocked.')
                    return HttpResponseRedirect(reverse_lazy('accounts:login'))
                else:
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
            else:
                messages.error(request, 'Invalid credentials')
                return HttpResponseRedirect(reverse_lazy('accounts:login'))
        else:
            return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        # Get the form value
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        username = str(first_name).lower() + "-" + str(last_name).lower()

        # Check if the passwords match
        if password == password1:
            # Check email
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already availible!")
                return HttpResponseRedirect(reverse_lazy('accounts:register'))
            else:
                # looks good
                user = User.objects.create_user(
                    username=username, first_name=first_name,
                    last_name=last_name, email=email, password=password,
                )
                user.save()

                # creating profile for the user
                profile = Profile.objects.get_or_create(user=user)
                profile.save()

                # login after register
                auth.login(
                    request, user, backend='accounts.EmailAuthenticationBackend.EmailBackend')
                messages.success(
                    request, "You are successfully registered; loged in")
                return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
        else:
            messages.error(request, "Passwords do not match!")
            return HttpResponseRedirect(reverse_lazy('accounts:register'))
    else:
        return render(request, "accounts/register.html")


@login_required
def dashboard(request):
    template = "accounts/dashboard.html"
    context = {}
    return render(request, template, context)


@login_required
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return HttpResponseRedirect(reverse_lazy("pages:home"))


def send_otp(request):
    if request.method == 'POST':
        api_key = settings.SMS_API_KEY
        sender = 'TXTLCL'
        number = request.POST.get('number')
        message = request.POST.get('otp')
        data = urllib.parse.urlencode({'apikey': api_key, 'numbers': number,
                                       'message': message, 'sender': sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        response = json.loads(fr).get('status')
        if response == 'success':
            return HttpResponseRedirect(reverse_lazy('otp verfication page.'))
        elif response.get('warnings')[0].get('code') == 3:
            messages.error("Please enter a valid phone number.")
            return HttpResponseRedirect(reverse_lazy("Phone number page."))
        else:
            messages.error(request, "OTP was not sent.")
            return HttpResponseRedirect(reverse_lazy("Phone number page."))

    template = 'account/register.html'
    context = {
        'response': response
    }
    return(request, template, context)


def view_profile(request):
    template = 'accounts/profile.html'
    context = {

    }
    return render(request, template, context)
