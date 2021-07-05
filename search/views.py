from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import search_history
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

class SearchView(APIView):
    def get(self, request):
        try:
            movies = search_history.objects.all()
        except search_history.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = SearchSerializers(movies, many=True)
            return Response(serializer_class.data)

class SearchAdd(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            data = request.data
            data['users'] = request.user.id
            serializer = SearchSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        try:
            movies = search_history.objects.get(id=pk)
            serializer = SearchSerializers(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            movies = search_history.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




