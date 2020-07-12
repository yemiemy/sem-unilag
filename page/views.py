from django.shortcuts import render, redirect
from datetime import datetime
from .models import Contact

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html', {'year':datetime.now().year})

def contact(request):
    if request.method == 'POST':
        fname = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        date_stamp = datetime.now()

        contact = Contact.objects.create(
            fname=fname,
            phone=phone,
            email=email, 
            message=message,
            date_stamp=date_stamp
            )
        contact.save()

        messages.success(request, 'Your message has been successfully sent! Thanks for reaching out.')

        context = {
            'fname':fname,
            'email':email,
            'message':message,
            'phone':phone
        }

        body = render_to_string('contact.txt', context)
        send_mail('Contact Form', body, 'rasholayemi@gmail.com', ['rasholayemi@gmail.com'])

        return redirect('index')

    return render(request, 'contact.html', {})