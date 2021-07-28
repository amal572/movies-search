from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import categories_film
from film.serializers import FilmSerializer,FilmOneSerializer,FilmTilte
from film.models import actors
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class CategoriesFilmView(APIView):
    def get(self, request):
        try:
            #movie=acotors_film.objects.filter(actor=actors.objects.get(id=actors))
            movies = categories_film.objects.all()
        except categories_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = categoriesSerializer(movies, many=True)
            return Response(serializer_class.data)

class FilmCategories(APIView):
    def get(self, request, pk):
        #print(pk)
        movies =categories_film.objects.filter(films=pk).filter(actors=pk)
        print(movies)
        serializers =categoriesSerializer(movies,many=True)
        return Response(serializers.data)

class CategoriesFilmAdd(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        try:
            serializer = categoriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoriesFilmUpdate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request,pk):
        try:
            movies = categories_film.objects.get(id=pk)
            serializer = categoriesSerializer(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoriesFilmDelete(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = categories_film.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




