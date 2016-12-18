from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'city', 'address', 'date', 'description', 'category', 'image', 'slug');
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
