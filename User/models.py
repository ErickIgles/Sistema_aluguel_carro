from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be is_superuser = True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    
    email = models.EmailField('e-mail', unique=True)
    first_name = models.CharField('First_name', max_length=200)
    last_name = models.CharField('Last_name', max_length=200)
    phone_number = models.CharField('Phone_number', max_length=11)
    cpf = models.CharField('cpf', max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    

    objects = UserManager()

    