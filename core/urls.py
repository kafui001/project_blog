from django.urls import path

from .views import HomeView, UserSignupView, Login

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]
