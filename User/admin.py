from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import *
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdim(UserAdmin):

    model = CustomUser

    # Definindo os formulários de edição e criação personalizados
    form = CustomUserChangeForm
    add_form = CustomUserCreateForm

    list_display = ('email', 'first_name', 'last_name', 'cpf')

    
    # Definindo os campos de edição detalhada para o formulário
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal Information', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined'), 'classes':('collapse',)})
    )


    # Definindo os filtros para pesquisa
    search_fields = ('email', 'first_name', 'last_name', 'cpf')
    ordering = ('email',)  # Ordenar por email

