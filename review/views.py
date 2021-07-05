from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import review_of_film
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class ReviewView(APIView):
    def get(self, request):
        try:
            movies = review_of_film.objects.all()
        except review_of_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = ReviewSerializers(movies, many=True)
            return Response(serializer_class.data)

class ReviewAdd(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            data = request.data
            data['users'] = request.user.id
            serializer = ReviewSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        try:
            movies = review_of_film.objects.get(id=pk)
            serializer = ReviewSerializers(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            movies = review_of_film.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




