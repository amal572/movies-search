from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from film.models import review_of_film,film
#from user.models import 
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import random

class ReviewView(APIView):
    def get(self, request):
        try:
            movies = review_of_film.objects.all()
        except review_of_film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            serializer_class = ReviewSerializers(movies, many=True)
            return Response(serializer_class.data)

class Add(APIView):
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
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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



class AddToDatabase(APIView):
    def post(self, request):
        try:
            data=request.data
            if film.objects.filter(title=data['film']).count():
                idd=request.data['user']
                names = random.choice(["abd", "silvi", "sherbel","amal","baraa"])
                
                if User.objects.filter(id=idd).count()==0:
                    username = names + str(idd)
                    email = username + str(idd) + '@gmail.com'
                    password = '1234'
                    user = User(id=idd,username=username,email=email)
                    user.set_password(password)
                    user.save()
                
                filmId = film.objects.filter(title=data['film']).values_list('id', flat=True)[0]
                re = review_of_film(users=User.objects.get(id=idd),films=film.objects.get(id=filmId),precent_rate=data['precent_rate'])
                re.save()
                return Response('ok')
            else:
                return Response('no film')
            
            return Response('any thing')
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
