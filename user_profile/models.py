from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
   username = None
   email = models.EmailField(_('email address'), unique = True)
   name = models.CharField(max_length = 100)
   bio = models.CharField(blank=True, null=True, max_length = 1000)
   profile_pic = models.ImageField(upload_to='images', blank=True, null=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['name']
   objects = CustomUserManager()
   def __str__(self):
       return "{}".format(self.email)
