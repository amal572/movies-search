from django.urls import path
from .views import searchApi

urlpatterns = [
    path('/SBert/<str:pk>/', searchApi.as_view()),
]