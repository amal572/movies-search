from rest_framework import serializers
from . models import film
from .models import actors
from .models import review_of_film
from .models import search_history
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = '__all__'



class FilmOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = ['id', 'title', 'director', 'description', 'release_date', 'run_time', 'spoken_language', 'rate']

class FilmTilte(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = ['title']

class FilmJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = ['id', 'title', 'director', 'description', 'release_date', 'run_time', 'spoken_language', 'rate']

class actorsOnSerializers(serializers.ModelSerializer):
    class Meta:
        model = actors
        fields = ['name']

class FilmReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = review_of_film
        fields = '__all__'

class search_historySerializers(serializers.ModelSerializer):
    class Meta:
        model = search_history
        fields = '__all__'