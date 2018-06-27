from django.conf.urls import url, re_path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from rest_framework import routers

app_name = 'groups'
router = routers.DefaultRouter()
router.register(r'', views.GroupViewSet)

urlpatterns = [
path(r'', views.ListGroup.as_view(), name='all'),
url(r'^list', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path('new/', views.CreateGroup.as_view(), name='create'),
path('posts/in/<slug:slug>/', views.SingleGroup.as_view(), name='single'),
path('join/<slug:slug>/', views.JoinGroup.as_view(), name='join'),
path('leave/<slug:slug>/', views.LeaveGroup.as_view(), name='leave'),

]