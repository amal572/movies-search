from rest_framework import serializers
from film.models import review_of_film

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = review_of_film
        fields = '__all__'

class ReviewOnSerializers(serializers.ModelSerializer):
    class Meta:
        model = review_of_film
        fields = ['precent']