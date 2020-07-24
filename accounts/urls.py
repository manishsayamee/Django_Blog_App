from django.urls import path
from .views import Signup_view, login_view, profile_view,logout_view, home

app_name = 'accounts'
urlpatterns=[
  path('signup/', Signup_view, name='signup'),
  path('login/', login_view, name='login'),
  path('profile/', profile_view, name='profile'),
  path('logout/', logout_view, name='logout'),

]