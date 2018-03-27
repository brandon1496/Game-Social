from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib import messages

from django.urls import reverse
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
# using LoginRequiredMixin cause the user needs to be logged in and once they join the group the RedirectView will redirect them somewhere else
class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    # Function apart of the RedirectView, takes user back to the SinglesGroup View
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        # Will attempt to add the user to the group by creating a new GroupMember
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            message.warning(self.request, ("Your already a member"))
        else:
            messages.success(self.request, ('Congrats your now a Member'))

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
     # Function apart of the RedirectView, takes user back to the SinglesGroup View
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!!!!')
        return super().get(request,*args,**kwargs)
    