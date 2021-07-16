from rest_framework import serializers
from film.models import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']