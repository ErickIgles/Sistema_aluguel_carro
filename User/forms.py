
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm

from .models import CustomUser


# Criar usuários junto com senha.
class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser

        labels = {'username': 'E-mail'}
        fields = ['email', 'cpf']
    

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.username = user.email
            user.save()
        return user
    


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'cpf']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'password' in self.fields:
            del self.fields['password']
    


class CustomLoginPage(AuthenticationForm):
    username = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder':'Digite o seu e-mail'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Digite a sua senha'}))


