from rest_framework import serializers
from film.models import categories

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'


class categoriesOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ['name']