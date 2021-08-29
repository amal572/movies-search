from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from director.serializers import DirectorOneSerializer
from categories.serializers import categoriesOneSerializer
from actors.serializers import actorsOnSerializers
from origin.serializers import originOnSerializers
from film.models import categories,actors,Director,origin,categories_film

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db import connection
import csv
class FiimView(APIView):
    def get(self, request):
        try:
            movies = film.objects.all()
        except film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = FilmSerializer(movies, many=True)
            return Response(serializer_class.data)

class FilmViewDetail(APIView):
    def get(self, request):
        try:
            movies = film.objects.all()
        except film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializers = FilmOneSerializer(movies, many=True)
            return Response(serializers.data)



class FilmCategories(APIView):
    def get(self, request, pk):
        movies = film.objects.get(id=pk)
        print(movies)
        mov = movies.categorie.all()
        print(mov)
        serializers = categoriesOneSerializer(mov, many=True)
        return Response(serializers.data)

class FilmOrigin(APIView):
    def get(self, request, pk):
        movies = origin.objects.filter(origin=pk)
        print(movies)
        serializers =originOnSerializers(movies,many=True)
        return Response(serializers.data)

class FilmDirector(APIView):
    def get(self, request, pk):
        #print(pk)
        movies =Director.objects.filter(director=pk)
        print(movies)
        serializers =DirectorOneSerializer(movies,many=True)
        return Response(serializers.data)

class FilmActors(APIView):
    def get(self, request, pk):
        # print(pk)
        movies = film.objects.get(id=pk)
        print(movies)
        mov = movies.actor.all()
        print(mov)
        serializers = actorsOnSerializers(mov, many=True)
        return Response(serializers.data)

class FilmReview(APIView):
    def get(self, request, pk):
        movies = film.objects.get(id=pk)
        mov = movies.review.through.objects.all()
        serializers = FilmReviewSerializers(mov , many=True)
        return Response(serializers.data)

class FilmSearch(APIView):
    def get(self, request, pk):
        #print(pk)
        movies = film.objects.get(id=pk)
        print(movies)
        mov = movies.search.through.objects.all()
        print(mov)
        serializers = search_historySerializers(mov , many=True)
        return Response(serializers.data)

class FilmAdd(APIView):
#    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        try:
            
            serializer = FilmSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                for x in request.data['categorie']:
                    obj=  categories_film(films=film.objects.get(id=serializer.data['id']),categori=categories.objects.get(id=x))
                    obj.save()
                for y in request.data['actor']:
                    obj1=  acotors_film(films=film.objects.get(id=serializer.data['id']),actors=actors.objects.get(id=y))
                    obj1.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FilmUpdate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = film.objects.get(id=pk)
            serializer = FilmSerializer(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
                for x in request.data['categorie']:
                    obj=  categories_film(films=film.objects.get(id=serializer.data['id']),categori=categories.objects.get(id=x))
                    obj.save()
                for y in request.data['actor']:
                    obj1=  acotors_film(films=film.objects.get(id=serializer.data['id']),actors=actors.objects.get(id=y))
                    obj1.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FilmDelete(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = film.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FilmAddToDatabase(APIView):
    def post(self, request, format=None):
        try:
            data=request.data
            origins_id=0
            if origin.objects.filter(name=data['origins']).count()==0:
                o = origin(name=data['origins'])
                o.save()
                data['origins']=o.id
            else:
                o = origin.objects.filter(name=data['origins']).values_list('id', flat=True)[0]
                data['origins']=o   
            
             
            dataCategorie=[]
            for x in request.data['categorie']:
                if categories.objects.filter(name=x).count()==0:
                    o = categories(name=x)
                    o.save()
                    dataCategorie.append(o.id)
                else:
                    o = categories.objects.filter(name=x).values_list('id', flat=True)[0]
                    dataCategorie.append(o)
                    

                    
            dataActors=[]        
            for y in request.data['actor']:
                if actors.objects.filter(name=y).count()==0:
                    o = actors(name=y)
                    o.save()
                    dataActors.append(o.id)
                else:
                    o = actors.objects.filter(name=y).values_list('id', flat=True)[0]
                    dataActors.append(o)
                

                    
                   
            serializer = FilmSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            for x in dataCategorie:
                obj=  categories_film(films=film.objects.get(id=serializer.data['id']),categori=categories.objects.get(id=x))
                obj.save()
            for y in dataActors:
                obj1=  acotors_film(films=film.objects.get(id=serializer.data['id']),actors=actors.objects.get(id=y))
                obj1.save()
            return Response('ok')
            
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)