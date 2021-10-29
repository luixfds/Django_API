from rest_framework import viewsets
from aliens.api import serializers
from aliens import models


class aliensViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlienSerializer
    queryset = models.Alien.objects.all()