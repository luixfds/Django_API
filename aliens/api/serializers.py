from rest_framework import serializers
from aliens import models


class AlienSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alien
        fields = '__all__'