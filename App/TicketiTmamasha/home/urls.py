from django.urls import path
from . import views

urlpatterns = [
   path('users/', views.all_users, name='all_users'),
]
