from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import acotors_film,film,actors
from film.serializers import FilmSerializer,FilmOneSerializer,FilmTilte
from actors.serializers import actorsSerializers,actorsOnSerializers
from film.models import actors
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class ActorsFilmView(APIView):
    def get(self, request):
        try:
            #movie=acotors_film.objects.filter(actor=actors.objects.get(id=actors))
            movies = acotors_film.objects.all()
        except acotors_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = actorsSerializers(movies, many=True)
            return Response(serializer_class.data)

class viewjoin(APIView):
    def get(self, request,pk):
        try:
            # movie=acotors_film.objects.filter(actor=actors.objects.get(id=actors))
            films =film.objects.filter(films=pk)
            print(films)
            actor = actors.objects.filter(actor=pk)
            print(actor)
        except acotors_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class1 = FilmTilte(films, many=True)
            serializer_class2 =actorsOnSerializers(actor,many=True)
            return Response(serializer_class1.data)

class FilmActors(APIView):
    def get(self, request, pk):
        #print(pk)
        movies =acotors_film.objects.filter(films=pk).filter(actors=pk)
        print(movies)
        serializers =actorsOnSerializers(movies,many=True)
        return Response(serializers.data)

class ActorsFilmAdd(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        try:
            serializer = actorsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActorsFilmUpdate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request,pk):
        try:
            movies = acotors_film.objects.get(id=pk)
            serializer = actorsSerializers(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActorsFilmDelete(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = acotors_film.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




