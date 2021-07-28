from django.urls import path
from .views import ActorsFilmView,ActorsFilmAdd,ActorsFilmUpdate,ActorsFilmDelete

urlpatterns = [
   path('view/', ActorsFilmView.as_view()),
   path('create/', ActorsFilmAdd.as_view()),
   path('update/<str:pk>/', ActorsFilmUpdate.as_view()),
   path('delete/<str:pk>/', ActorsFilmDelete.as_view()),
]