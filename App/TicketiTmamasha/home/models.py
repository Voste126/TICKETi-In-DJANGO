import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.email + '  ' + self.password

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.description + ' ' + self.venue + ' ' + str(self.date) + ' ' + str(self.time)

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name + ' ' + str(self.price) + '    ' + str(self.event)
    
class EventCalender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '   ' + self.description + '    ' + self.venue + '     ' + str(self.date) + '   ' + str(self.time)
