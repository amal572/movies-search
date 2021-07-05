from rest_framework import serializers
from film.models import like_un_like_film

class InteractSerializers(serializers.ModelSerializer):
    class Meta:
        model = like_un_like_film
        fields = '__all__'
