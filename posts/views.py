from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    #Shows the posts related to the user or group
    select_related = ('user', 'group')

class UserPosts(generic.ListView):
    model = models.Post
    template_name= "posts/UserPost_list.html"

    #gets username of whoever is currently signed in right now 
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

# Class to create posts
class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Post
    fields = ('message', 'group')
    
    #overriding the form_valid function making sure that the new post is connected to the user that made it
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

# Class to Delete posts
class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    template_name = "posts/post_confirm_delete.html"
    # after post is deleted it will send the user to posts:all
    success_url = reverse_lazy('posts:all')

    
    # Will display to the  user that the Post was Deleted
    
