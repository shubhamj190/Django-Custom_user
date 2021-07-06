from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class Account(AbstractUser):
    # If we use say AbstractBaseUser then we have to give permissionMixiin that is
    username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=200, blank=True, null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
