from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

#Create your views here.
class HomeView(FormView):
    template_name = 'core/home.html'
    form_class = ContactForm
    success_url = 'home'
