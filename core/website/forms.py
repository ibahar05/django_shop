from django import forms 
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","phone_number","subject","message"]

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ["email"]


