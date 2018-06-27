from rest_framework import serializers
from groups.models import Group
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):    
     class Meta:
        model = User
        fields = ('id', 'username', 'email')
