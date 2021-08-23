from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
        ListView, CreateView, DetailView, DeleteView, UpdateView, FormView, View
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



class BlogSingleView(View):

    def get(self, request, pk, **kwargs):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.select_related('post').all()
        return render(request,'blog/blog_detail.html', {'post':post, 'comment':comments,'comment_form':CommentForm}) 

    def post(self, request,pk,*args, **kwargs):
        comment_form = CommentForm(self.request.POST or None)
        post_instance = Post.objects.get(id=pk)
        
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.author = self.request.user
            user_comment.post = post_instance
            user_comment.save()
            return HttpResponseRedirect('/blog/detail/' + str(post_instance.pk))


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_home')


class BlogEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_edit.html'
    success_url = reverse_lazy('detail_blog')

