from rest_framework import routers
from django.urls import path, include
from .views import EventViewSet, private_view, register_event, unregister_event

router = routers.DefaultRouter()
router.register('api/event', EventViewSet, 'events')

urlpatterns = [
    path('', include(router.urls)),
    path('api/private_event', private_view),
    path('api/register_event/<int:pk>', register_event),
    path('api/unregister_event/<int:pk>', register_event),
]
