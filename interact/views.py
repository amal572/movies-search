from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import like_un_like_film
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class InteractView(APIView):
    def get(self, request):
        try:
            movies = like_un_like_film.objects.all()
        except like_un_like_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = InteractSerializers(movies, many=True)
            return Response(serializer_class.data)

class InteractAdd(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            data = request.data
            data['users'] = request.user.id
            serializer = InteractSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InteractUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        try:
            movies = like_un_like_film.objects.get(id=pk)
            serializer = InteractSerializers(instance=movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InteractDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            movies = like_un_like_film.objects.get(id=pk)
            movies.delete()
            return Response("Item succsesfully Delete")
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




