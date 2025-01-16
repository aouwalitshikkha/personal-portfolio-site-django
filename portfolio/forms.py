from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "Enter your name",
                'required':'required'
            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': "Your email address",
                'required': 'required'
            }),
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Enter the discussion title",
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Write your message",
                'required': 'required'
            })

        }