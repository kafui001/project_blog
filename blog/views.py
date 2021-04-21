from django.shortcuts import render
from django.views.generic import ListView, CreateView


from .models import Post, Category
from .forms import PostForm
# Create your views here.
# def bloghome(request):
#     return render(request, 'blog/blog_home.html')

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    ordering = ['-date_created']

class BlogAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'