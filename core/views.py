from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

# Create your views here.
# def home(request):
#     print(ContactForm)
#     return render(request, 'core/home.html',{'form': ContactForm})
    

class HomeView(FormView):
    template_name = 'core/home.html'
    form_class = ContactForm
    print(ContactForm)
    success_url = 'home'
