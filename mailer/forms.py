from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    """Form for subscribing on email spamming"""

    class Meta:
        model = Contacts
        fields = '__all__'
