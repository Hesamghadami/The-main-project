from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    #path('category/<str:cat>', blog_home , name= 'blog_home_with_category'),
    path('post_details/<int:pid>', blog_single , name='blog_single'),
]