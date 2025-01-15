from django.shortcuts import render
from .models import Education, Experiences, Services, Skills, PersonalDetails, Welcome
# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    details = PersonalDetails.objects.first()
    skills = Skills.objects.all()

    return render(request, 'portfolio/about.html', {'details': details, 'skills': skills})

def contact(request):
    return render(request, 'portfolio/contact.html')

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
    return render(request, 'portfolio/works.html')


def services(request):
    services = Services.objects.all()[:5]
    return render(request, 'portfolio/services.html', {'services': services})