from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import urllib.request
import urllib.parse
import json
from django.conf import settings
from .models import Profile, Address
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.http import is_safe_url
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
    else:
        if request.method == 'POST':
            # Login User
            email_phone = request.POST.get('email_phone')
            password = request.POST.get('pass')

            redirect_url_path = request.POST.get('next') or None

            user = auth.authenticate(username=email_phone, password=password)

            if user is not None:
                if user.profile.blocked:
                    messages.error(
                        request, 'Your account has been blocked.')
                    return HttpResponseRedirect(reverse_lazy('accounts:login'))
                else:
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    if redirect_url_path != 'None':
                        if is_safe_url(redirect_url_path, request.get_host()):
                            return HttpResponseRedirect(redirect_url_path)
                    else:
                        return HttpResponseRedirect(reverse_lazy('accounts:dashboard'))
            else:
                messages.error(request, 'Invalid credentials')
                return HttpResponseRedirect(reverse_lazy('accounts:login'))
        else:
            next_url = request.GET.get('next')
            return render(request, 'accounts/login.html', {"next_url": next_url})


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


@login_required
def view_profile(request):
    template = 'accounts/profile.html'
    return render(request, template)


@login_required
def add_address(request):
    if request.method == "POST":
        user = request.user
        address_type = request.POST.get("address-type")
        address = request.POST.get("address")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip-code")

        new_address = Address.objects.create(
            user=user, address_type=address_type, address=address,
            country=country, state=state, city=city, zip_code=zip_code
        )

        new_address.save()
        messages.success(request, "New address was successfully added.")
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def update_address(request, address_id):
    if request.method == "POST":
        user = request.user
        address_type = request.POST.get("address-type")
        address = request.POST.get("address")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip-code")

        address_fetched = get_object_or_404(Address, id=address_id, user=user)
        address_fetched.address_type = address_type
        address_fetched.address = address
        address_fetched.country = country
        address_fetched.state = state
        address_fetched.city = city
        address_fetched.zip_code = zip_code
        address_fetched.save()
        messages.success(request, "Your address was successfully updated.")
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    address.delete()
    messages.success(request, "Address was successfully deleted.")
    return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def update_personal_details(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first-name')
        last_name = request.POST.get("last-name")
        dob = request.POST.get('dob')
        gender = request.POST.get("gender")

        user.first_name = first_name
        user.last_name = last_name

        profile = Profile.objects.get(user=user)
        profile.date_of_birth = dob
        profile.gender = gender
        profile.save()
        user.save()
        messages.success(request, "Personal details has been updated.")
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def update_accounts_status(request):
    if request.method == "POST":
        user = request.user
        status = request.POST.get("active-status")
        if status == "0":
            user.is_active = False
            user.save()
            auth.logout(request)
            messages.error(request, 'Your account has beeen deactivated')
            return HttpResponseRedirect(reverse_lazy("accounts:login"))
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def update_email(request):
    if request.method == "POST":
        user = request.user
        email = request.POST.get('email')
        user.email = email
        user.save()
        messages.success(request, "Your email has been updated.")
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def add_phone(request):
    if request.method == "POST":
        user = request.user
        phone = request.POST.get('phone')
        profile = Profile.objects.get(user=user)
        profile.phone = phone
        profile.save()
        messages.success(request, "Your phone has been updated.")
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been updated.")
            return HttpResponseRedirect(reverse_lazy("accounts:view_profile"))
        # else:
        #     messages.error(request, "blablanblab")
        #     return HttpResponseRedirect('/accounts/profile/#change-password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "accounts/form.html", {'form': form})
