from django.shortcuts import render,redirect
from .forms import SignUp, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

USER = get_user_model()



def Signup_view(request):
  if request.method == "POST":
    form = SignUp(request.POST)
    if form.is_valid():
      print("form is valid")
      print(form.cleaned_data)

      user = USER(
        username = form.cleaned_data['username'],
        email = form.cleaned_data['email'], 
        first_name = form.cleaned_data['first_name'],
        last_name = form.cleaned_data['last_name'],
      
      )

      user.save()
      user.set_password(form.cleaned_data['password'])
      user.save()

      logout(request)
      login(request, user)

      return redirect('/accounts/login')

  elif request.method == "GET":
    form = SignUp()
  
  return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
  if request.method == "POST":
    form  = LoginForm(request.POST)
    if form.is_valid():
      print("Form is valid")
      print(form.cleaned_data)

      user = authenticate(
        email = form.cleaned_data['email'],
        password = form.cleaned_data['password']

      )
      if user:
        print("the user is authenticated")
        login(request, user)
        return redirect('/accounts/profile')
      else:
        print("the user is not authenticated")
  elif request.method == "GET":
    if request.user.is_authenticated:
      return redirect('/accounts/profile/')
    form = LoginForm()

  return render(request, 'accounts/login.html', {'form':form})
@login_required()
def profile_view(request):
  from myblog.models import Blog
  # message = Blog.objects.filter(author=request.user)
  message = Blog.objects.all()
  return render(request, 'accounts/profile.html', {'message':message})

def logout_view(request):
  logout(request)
  return redirect('/accounts/login')

def home(request):
  return render(request, 'accounts/home.html')
  






