from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def private_view(request,format=None):
  queryset = Event.objects.filter(private=True,invited_users=request.user).select_related('created_by').prefetch_related('invited_users','registered_users')
  serializer = EventSerializer(queryset,many=True)
  return Response(serializer.data)

class EventPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
      if view.action in ['list', 'retrieve']:
        return True
      else:
        if request.user.is_authenticated:
          return True
        else:
          return False  


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [
        EventPermission,
    ]
    queryset = Event.objects.filter(private=False).select_related(
        'created_by').prefetch_related('invited_users', 'registered_users')
    serializer_class = EventSerializer


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def register_event(request,pk, format=None):
  try:
    event = Event.objects.get(pk=pk)
    other_events = Event.objects.filter(schedule=event.schedule, registered_users=request.user).select_related(
        'created_by').prefetch_related('invited_users', 'registered_users').exists()
    if event.registered_users.all().count() == event.no_of_attendees:
      return Response("Attendees limit reached") 
    if not other_events:
      event.registered_users.add(request.user)
    else:
      return Response("schedule overlapped with other event")  
  except EventDoesNotExist:
    event = None  
  serializer = EventSerializer(event)
  return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def unregister_event(request, pk, format=None):
  try:
    event = Event.objects.get(pk=pk)
    event.registered_users.remove(request.user)
  except EventDoesNotExist:
    event = None
  serializer = EventSerializer(event)
  return Response(serializer.data)


