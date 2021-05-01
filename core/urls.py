from django.urls import path

from .views import HomeView, UserSignupView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('signup/', UserSignupView.as_view(), name='signup'),
]
