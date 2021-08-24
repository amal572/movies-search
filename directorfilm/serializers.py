from rest_framework import serializers
from film.models import director_film

class directorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = director_film
        fields = '__all__'