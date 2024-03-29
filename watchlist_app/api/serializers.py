from rest_framework import serializers
from watchlist_app.models import Movie


class Moviserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()