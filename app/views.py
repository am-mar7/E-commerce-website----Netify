from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm 
from django.conf import settings
from .models import Package

def home(request):
    packages = list(Package.objects.all())
    return render(request , 'pages/home.html' , {
        'packages':packages
    })

def about(request):
    return render(request , 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = f"New Contact Message from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]  

            send_mail(subject, message, from_email, recipient_list)

            return redirect('home')  
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})


