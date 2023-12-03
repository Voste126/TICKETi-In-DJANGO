from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Event, Ticket, EventCalender
from .serializers import UserSerializer, EventSerializer, TicketSerializer, EventCalenderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api to get a specific user
@api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#getting all the users in the system
@api_view (['GET', 'POST', 'DELETE'])
def all_events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        events = Event.objects.all()
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#getting all tickets available for events    
@api_view (['GET', 'POST', 'DELETE'])
def all_tickets(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        tickets = Ticket.objects.all()
        tickets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#getting all events_calenders in the system
@api_view (['GET', 'POST', 'DELETE'])
def all_event_calenders(request):
    if request.method == 'GET':
        event_calenders = EventCalender.objects.all()
        serializer = EventCalenderSerializer(event_calenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = EventCalenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        event_calenders = EventCalender.objects.all()
        event_calenders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# get all user
#serialize the data
#return the data as json
