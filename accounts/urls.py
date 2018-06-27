from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.urls import path, re_path
from . import views

app_name = 'accounts'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
url(r'^', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', views.SignUp.as_view(), name='signup'),


]