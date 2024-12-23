from rest_framework import serializers
from .models import Event, Attendee, Task

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    attendees = AttendeeSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
