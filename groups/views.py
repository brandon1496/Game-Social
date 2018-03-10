from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)

from django.utils import reverse
from django.views import generic
from groups.models import Group, GroupMember

# Create your views here.
# Class to create a group
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'message')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group
# List out the groups
class ListGroup(generic.ListView):
    model = Group