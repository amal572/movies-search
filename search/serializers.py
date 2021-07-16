from rest_framework import serializers
from film.models import search_history

class SearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = search_history
        fields = '__all__'

class SearchOnSerializers(serializers.ModelSerializer):
    class Meta:
        model = search_history
        fields = ['Text']