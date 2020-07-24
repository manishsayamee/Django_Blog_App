from django.forms import ModelForm
from .models import Blog


class BlogDetail(ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'text', 'author']