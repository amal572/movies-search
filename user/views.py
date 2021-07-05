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
        #username = request.data['username']
        #password = request.data['password']
        #user = User(username=username)
        #user.set_password(password)
        #user.save()
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
