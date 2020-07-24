from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import CustomUser

class Blog(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  text = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)


  def __str__ (self):

    return self.title

