from django.urls import path

from .views import HomeView #, UserSignupView, UserLogin, UserLogout



urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    
    # path('signup/', UserSignupView.as_view(), name='signup'),
    # path('login/', UserLogin.as_view(), name='login'),
    # path('logout/', UserLogout.as_view(), name='logout'),
    
]
