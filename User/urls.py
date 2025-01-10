
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TemplateRegisterUser.as_view(), name='register_user'),
    path('loginPage/', LoginPage.as_view(), name='loginpage'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home', Home.as_view(), name='home'),
]
