from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

from blog.models import Post
#Create your views here.

class HomeView(FormView):
    template_name = 'core/home.html'
    form_class = ContactForm
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['recent_blog'] = Post.objects.order_by('-date_created')[:3]
        return context
