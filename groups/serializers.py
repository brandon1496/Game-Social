from rest_framework import serializers
from groups.models import Group

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
   
    class Meta:
        model = Group
        fields = ('name', 'info', 'members')
