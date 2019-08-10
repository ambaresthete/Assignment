from django.db import models
from django.conf import settings
from django.utils import timezone
User = settings.AUTH_USER_MODEL

# Create your models here.

class Event(models.Model):
  created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_by")
  no_of_attendees = models.IntegerField(null=True,blank=True)
  invited_users = models.ManyToManyField(User,blank=True,related_name="invited")
  private = models.BooleanField(default=False)
  registered_users = models.ManyToManyField(User,blank=True,related_name="registered")
  schedule = models.DateField(default=timezone.now)

