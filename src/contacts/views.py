from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        client_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        redirect_url = request.POST.get('redirect')
        print(redirect_url)

        contact = Contact(name=name, subject=subject,
                          email=client_email, message=message)
        contact.save()

        # Send email to support team
        send_mail(
            'Client Inquiry',
            'There has been an inquiry regarding to DANGUI STAMP MAKERS. Sign into the admin panel for more info.',
            'danguistamp@gmail.com',
            ['azizrahman.yarzai0@gmail.com'],
            fail_silently=False
        )

        # Send email to customer
        send_mail(
            'Repaly for your inquiry',
            'Thank You ' + name + ' for your inquiry. Our support team will reach you soon.',
            'danguistamp@gmail.com',
            [client_email],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, our support team will get back to you soon')
        return redirect(redirect_url)
