from django.urls import path
from . import views

urlpatterns = [
   path('users/', views.all_users, name='all_users'),
   path('events/', views.all_events, name='all_events'),
   path('tickets/', views.all_tickets, name='all_tickets'),
   path('event_calenders/', views.all_event_calenders, name='all_event_calenders'),
   path('users/<int:pk>/', views.get_user, name='user_detail'),
]
