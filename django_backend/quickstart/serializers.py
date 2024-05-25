from django.contrib.auth.models import Group, User
from rest_framework import serializers

from habit_tracker.serializers import HabitSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'habits']
        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        