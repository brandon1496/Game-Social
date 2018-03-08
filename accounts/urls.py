from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

path('Login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
path('Logout/', auth_views.LogoutView.as_view(), name='logout'),
path('Signup/', views.SignUp.as_view(), name='signup'),


]