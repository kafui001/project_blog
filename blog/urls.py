from django.urls import path

from .views import bloghome

urlpatterns = [
    path('', bloghome, name='blog_home'),
]
