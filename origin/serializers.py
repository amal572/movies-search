from rest_framework import serializers
from film.models import origin

class originSerializers(serializers.ModelSerializer):
    class Meta:
        model = origin
        fields = '__all__'

class originOnSerializers(serializers.ModelSerializer):
    class Meta:
        model = origin
        fields = ['name']

