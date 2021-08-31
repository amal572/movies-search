from django.urls import path
from .views import searchApi

urlpatterns = [
    path('/SBert', searchApi.as_view()),
]