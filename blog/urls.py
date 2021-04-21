
from django.urls import path
from .views import BlogHomeView, BlogAddView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('add/', BlogAddView.as_view(), name='add_blog'),
]
