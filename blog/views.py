from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
        ListView, CreateView, DetailView, DeleteView, UpdateView
    )


from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from core.forms import ContactForm


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    ordering = ['-date_created']
    paginate_by = 2

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


class BlogSingleView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogSingleView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['comment_form'] = CommentForm
        return context 


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_home')


class BlogEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_edit.html'
    success_url = reverse_lazy('detail_blog')

