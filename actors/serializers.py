from rest_framework import serializers
from film.models import actors

class actorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = actors
        fields = '__all__'

class actorsOnSerializers(serializers.ModelSerializer):
    class Meta:
        model = actors
        fields = ['name']

