from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import actors
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class ActorsView(APIView):
    def get(self, request):
        try:
            movies = actors.objects.all()
        except actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = actorsSerializers(movies, many=True)
            return Response(serializer_class.data)

class ActorsViewDetail(APIView):
    def get(self,request):
        try:
            movies = actors.objects.all()
        except actors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializers = actorsOnSerializers(movies, many=True)
            return Response(serializers.data)


class ActorsAdd(APIView):
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

class ActorsUpdate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request,pk):
        try:
            movies = actors.objects.get(id=pk)
            serializer = actorsSerializers(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActorsDelete(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        try:
            movies = actors.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


