from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView,View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.core.mail import send_mail

# from .forms import ContactForm

from blog.models import Post
#Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {'recent_blog' : Post.objects.order_by('-date_created')[:3]}
        return render(request,'core/home.html',context)
        
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.request.POST
            
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            my_email = 'kafui01@yahoo.com'
            message = form['message']
            subject = f"MESSAGE from kafuiahedor.com: sender -- {first_name} {last_name}"
            final_message = f"{message}\n --------\n message coming from {first_name} {last_name}\n who's email address is {email}"
            send_mail(
                subject, # subject of message
                final_message, # message
                my_email, # from email
                ['kafui01@yahoo.com'], # to email
            )
            return redirect('home')

class UserSignupView(CreateView):
    form_class = UserCreationForm
    template_name = "core/signup.html"
    success_url = reverse_lazy('blog_home')


class UserLogin(FormView):
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

class UserLogout(FormView):

    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("blog_home")