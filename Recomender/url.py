from django.urls import path
from .views import trainingRecomender, getRecomender, getMaxFilm,traningCollaborative1, traningCollaborative2,expertMovie,expertRate

urlpatterns = [
   path('train/', trainingRecomender.as_view()),
   path('view/<str:pk>/', getRecomender.as_view()),
   path('MaxFilm/', getMaxFilm.as_view()),
   path('traningCollaborative1', traningCollaborative1.as_view()),
   path('traningCollaborative2', traningCollaborative2.as_view()),
   path('expertMovie/', expertMovie.as_view()),
   path('expertRate/', expertRate.as_view()),
]