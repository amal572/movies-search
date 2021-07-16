from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/' , RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]