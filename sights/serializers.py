from rest_framework import serializers
from .models import Sight


class SightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sight
        fields = ('title', 'slug', 'description', 'photo', 'latitude', 'longitude')
