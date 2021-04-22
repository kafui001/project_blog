from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView


from .models import Post, Category
from .forms import PostForm
from core.forms import ContactForm


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    ordering = ['-date_created']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['form'] = ContactForm
        return context 

class BlogAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_create.html'


    def get_success_url(self):
        return reverse('blog_home')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.author = self.request.user
        form.save()
        return super(BlogAddView, self).form_valid(form)