from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
#from accounts.models import User
from django.contrib.auth.models import User
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer