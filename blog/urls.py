
from django.urls import path
from .views import BlogHomeView, BlogAddView, BlogSingleView, blogDeleteView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('add/', BlogAddView.as_view(), name='add_blog'),
    path('detail/<int:pk>', BlogSingleView.as_view(), name='detail_blog'),
    path('delete/<int:pk>', blogDeleteView.as_view(), name='delete_blog'),
]
