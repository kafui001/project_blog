import requests

from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView,View
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.core.mail import send_mail


from project_blog.settings import MAILGUN_API_KEY,MAILGUN_DOMAIN

import smtplib

from email.mime.text import MIMEText
# from .forms import ContactForm

# from blog.models import Post
#Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # context = {'recent_blog' : Post.objects.order_by('-date_created')[:3]}
        # return render(request,'core/home.html',context)
        return render(request,'core/home.html')

    # def send_simple_message( first_name,last_name,from_email,my_email,message,api_key, domain):
    #     send_email = requests.post(
    #         f"https://api.mailgun.net/v3/{domain}/messages",
    #         auth=("api", api_key),
    #         data={"from": from_email,
    #             "to": [my_email],
    #             "subject": f"MESSAGE from kafuiahedor.com: sender -- {first_name} {last_name}",
    #             "text": message})

    #     return send_email
        
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.request.POST
            
            first_name = form['first_name']
            last_name = form['last_name']
            from_email = form['email']
            my_email = 'kafui01@yahoo.com'
            message = form['message']
            # subject = f"MESSAGE from kafuiahedor.com: sender -- {first_name} {last_name}"
            # final_message = f"{message}\n --------\n message coming from {first_name} {last_name}\n who's email address is {email}"
            # send_mail(
            #     subject, # subject of message
            #     final_message, # message
            #     my_email, # from email
            #     ['kafui01@yahoo.com'], # to email
            # )
            ## MAILGUN API 
            # send_email = requests.post(
            #         f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            #         auth=("api", MAILGUN_API_KEY),
            #         data={"from": f"Excited User mailgun@{MAILGUN_DOMAIN}",
            #             "to": [my_email,f"kafui@{MAILGUN_DOMAIN}"],
            #             "subject": f"MESSAGE from kafuiahedor.com: sender -- {first_name} {last_name}",
            #             "text": f"{message}\n --------\n message coming from {first_name} {last_name}\n who's email address is {from_email}"})


            msg = MIMEText(f"{message}\n --------\n message coming from {first_name} {last_name}\n who's email address is {from_email}")
            msg['Subject'] = f"MESSAGE from kafuiahedor.com: sender -- {first_name} {last_name}"
            msg['From']    = f"kafui@{MAILGUN_DOMAIN}"
            msg['To']      = my_email

            s = smtplib.SMTP('smtp.mailgun.org', 587)

            s.login(f'postmaster@{MAILGUN_DOMAIN}', '3kh9umujora5')
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
            return redirect('home')


            


'''
# BLOG FEATURES
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
'''
