from django.db import models
# Remove spaces in string to use in url
from django.utils.text import slugify
# Call things off the user current session
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()


# Allows for a link between the post and Groupmember so we could use "get"
from django import template
register = template.Library()

class Group(models.Model):
    # 
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    info = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember', related_name='people')
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)
    def __str__(self):

        return self.user.username 

    class Meta:
        # Makes sure that they are different from each other
        unique_together = ('group', 'user')