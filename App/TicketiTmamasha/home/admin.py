from django.contrib import admin

# Register your models here.
from .models import User, Event, Ticket, EventCalender

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(EventCalender)

