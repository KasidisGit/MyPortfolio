from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm


def index(request):
    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.contact_email=form.cleaned_data['contact_email']
            form.contact_subject=form.cleaned_data['contact_subject']
            form.contact_message=form.cleaned_data['contact_message']
            form.save()
    return render(request, 'index.html', {'form': form})
