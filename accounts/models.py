from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  email = models.CharField(max_length=150, unique=True, blank=False)

  def __str__(self):
    return self.email

  groups = None
  user_permissions = None

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  
