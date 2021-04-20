from django.shortcuts import render
from django.views.generic import ListView


from .models import Post, Category

# Create your views here.
# def bloghome(request):
#     return render(request, 'blog/blog_home.html')

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    ordering = ['-date_created']