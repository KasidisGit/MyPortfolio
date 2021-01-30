from django import forms
from .models import Form

class ContactForm(forms.ModelForm):
    contact_email = forms.EmailField(label='Your Email')
    contact_subject = forms.CharField(label='Your Subject', max_length=100)
    contact_message = forms.CharField(label='Message...')

    class Meta:
        model = Form
        fields = ('contact_email', 'contact_subject', 'contact_message')
