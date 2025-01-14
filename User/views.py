from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreateForm, CustomLoginPage
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class TemplateRegisterUser(FormView):
    model = CustomUser
    template_name ='register.html'
    form_class = CustomUserCreateForm
    success_url = 'home'

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



class LoginPage(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginPage


    def get_success_url(self):
        
        return reverse_lazy('home')


    