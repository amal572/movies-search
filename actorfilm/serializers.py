from rest_framework import serializers
from film.models import acotors_film

class actorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = acotors_film
        fields = '__all__'


