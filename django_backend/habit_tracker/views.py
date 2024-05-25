from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from habit_tracker.serializers import HabitSerializer
from habit_tracker.models import Habit

class HabitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows habits to be viewed or editied
    """
    serializer_class = HabitSerializer
    
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

