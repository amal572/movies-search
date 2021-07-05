from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import Director
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class DirectorView(APIView):
    def get(self, request):
        try:
            movies = Director.objects.all()
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = DirectorSerializer(movies, many=True)
            return Response(serializer_class.data)

class DirectorViewDetail(APIView):
    def get(self, request):
        try:
            movies = Director.objects.all()
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializers = DirectorOneSerializer(movies, many=True)
            return Response(serializers.data)

class DirectorAdd(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        try:
            serializer = DirectorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DirectorUpdate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request,pk):
        try:
            movies = Director.objects.get(id=pk)
            serializer = DirectorSerializer(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DirectorDelete(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = Director.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


