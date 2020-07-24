from django.shortcuts import render
from .forms import BlogDetail
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView


@method_decorator(login_required, name = "dispatch")
class createBlog(CreateView):
  form_class = BlogDetail
  template_name = 'myblog/create.html'
  success_url = '/accounts/profile/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user =  self.request.user
    self.object.save()
    return super().form_valid(form)

class DeleteBlog(DeleteView):
  model = BlogDetail.Meta.model
  success_url = '/myblog/allblog/'

  def get_queryset(self):
    return Blog.objects.filter(
      author = self.request.user
    )

  def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)


class UpdatedBlog(UpdateView):
  form_class = BlogDetail
  pk_url_kwarg = 'id'
  success_url = '/accounts/profile/'
  model = Blog
  template_name = 'myblog/update.html'
  
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return super().form_valid(form)


class AllBlog(ListView):
  model = Blog
  template_name = 'myblog/index.html'
  context_object_name ='data'

def detail(request, pk):
  user_obj = Blog.objects.get(id=pk)
  return render(request, 'myblog/post_detail.html', context={
    'data':user_obj
  })

