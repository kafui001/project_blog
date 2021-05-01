from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

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


class UserSignupView(CreateView):
    form_class = UserCreationForm
    template_name = "core/signup.html"
    success_url = reverse_lazy('blog_home')


class Login(FormView):
    template_name = "core/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            user = form.get_user()
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)