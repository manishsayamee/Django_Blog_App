from django.urls import path
from .views import createBlog, DeleteBlog, UpdatedBlog, AllBlog,detail
app_name = 'myblog'
urlpatterns =[
  path('create/', createBlog.as_view(), name='create'),
  path('delete/<int:pk>/',DeleteBlog.as_view(), name='delete'),
  path('update/<int:pk>/',UpdatedBlog.as_view(), name='update'),
  path('allblog/', AllBlog.as_view(), name='all'),
  path('detail/<int:pk>/', detail, name='detail'),
] 