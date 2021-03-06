from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer
    lookup_field = 'slug'
