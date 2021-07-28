from rest_framework import serializers
from film.models import categories_film

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories_film
        fields = '__all__'

