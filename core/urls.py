from django.urls import path

from .views import HomeView, bloghome

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('blog/', bloghome, name='blog-home'),
]
