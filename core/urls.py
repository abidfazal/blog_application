from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('authorposts/<str:author>',views.post_of_an_author,name='authorposts'),
    path('details/<int:pk>',views.blog_details,name='details'),
    path('addblog/',views.add_blog,name='addblog'),
    path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name='login.html'),name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('logout',views.log_out,name='logout'),
]
