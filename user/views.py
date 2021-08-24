from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import RegisterSerializer,ChangePasswordSerializer
from rest_framework import generics, permissions
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if (serializer.is_valid()):
           user = serializer.save()
#        id = '1236'
#        username = 'abd'
#        email = 'abd@gmail.com'
#        password = request.data['password']
#        user = User(id=id,username=username,email=email)
#        user.set_password(password)
#        user.save()
        refresh = RefreshToken.for_user(user)
        return JsonResponse(
            {
                "status": "success",
                'user_id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    #@detail_route(methods='PUT')
#    def perform_update(self, serializer):
#        try:
#            if request.method == "PUT":
#                 serializer.save(user=self.request.user.id)
#        except film.DoesNotExist:
#            return Response(status=status.HTTP_404_NOT_FOUND)
       
    
class personalInfo(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = request.data 
        user={'id':request.user.id,'username':request.user.username,'email':request.user.email}
        return Response(user)
#      