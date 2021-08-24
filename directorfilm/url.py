from django.urls import path
from .views import directorFilmView,directorFilmAdd,directorFilmUpdate,directorFilmDelete

urlpatterns = [
   path('view/', directorFilmView.as_view()),
   path('create/', directorFilmAdd.as_view()),
   path('update/<str:pk>/', directorFilmUpdate.as_view()),
   path('delete/<str:pk>/', directorFilmDelete.as_view()),
]