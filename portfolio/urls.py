from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('services/', services, name='services'),
    path('testimonial/', testimonial, name='testimonial'),
    path('welcome/', welcome, name='welcome'),
    path('works/', works, name='works'),
]