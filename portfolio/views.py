from django.shortcuts import render, redirect
from .models import Education, Experiences, Services, Skills, PersonalDetails, Welcome, Works
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    details = PersonalDetails.objects.first()
    skills = Skills.objects.all()

    return render(request, 'portfolio/about.html', {'details': details, 'skills': skills})

def contact(request):
    email = 'aouwalcmc@gmail.com'
    phone = '017100420400'
    skype = 'aouwalitshikkha'
    social = {'fb':'https://www.facebook.com/itshikkha', 'twitter': 'https://twitter.com/itshikkha'}

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message was sent successfully")
            return redirect('contact')

        else:
            messages.error(request, "Something went wrong, please try again later")

    else:
        form = ContactForm()

    context = {'form': form, 'email': email, 'phone': phone,'skype':skype, 'social':social}



    return render(request, 'portfolio/contact.html', context)

def resume(request):
    education = Education.objects.all()
    experiences = Experiences.objects.all()
    context = {
        'educations': education,
        'experiences': experiences,
    }
    return render(request, 'portfolio/resume.html', context)

def testimonial(request):
    return render(request, 'portfolio/testimonial.html')

def welcome(request):
    welcome = Welcome.objects.first()
    return render(request, 'portfolio/welcome.html', {'welcome':welcome})

def works(request):
    works = Works.objects.all()
    return render(request, 'portfolio/works.html', {'works': works})


def services(request):
    services = Services.objects.all()[:5]
    return render(request, 'portfolio/services.html', {'services': services})