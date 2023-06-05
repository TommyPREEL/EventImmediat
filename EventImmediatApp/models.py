from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

# Events models
class Events(models.Model):
    id_events = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='id_creator')
    date_start = models.DateField()
    date_end = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

# EventsParticipants models : the table between the events and the users who participate to the events
class EventsParticipants(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('event', 'user'),)