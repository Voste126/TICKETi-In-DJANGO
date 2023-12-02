#where serialization of the models.py file are done
from rest_framework import serializers
from .models import User, Event, Ticket, EventCalender

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'time', 'venue', 'image', 'user']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'name', 'price', 'event']

class EventCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCalender
        fields = ['id', 'name', 'description', 'date', 'time', 'venue', 'image', 'user']