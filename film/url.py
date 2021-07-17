from django.urls import path
from .views import FiimView, FilmViewDetail, FilmAdd, FilmUpdate, FilmDelete,FilmCategories,FilmDirector,FilmActors,FilmReview,FilmSearch,FilmOrigin
from . import views

urlpatterns = [
   path('view/', FiimView.as_view()),
   path('viewDetail/', FilmViewDetail.as_view()),
   path('viewCategories/<str:pk>/', FilmCategories.as_view()),
   path('viewOrigin/<str:pk>/', FilmOrigin.as_view()),
   path('viewDirector/<str:pk>/', FilmDirector.as_view()),
   path('ViewActor/<str:pk>/',FilmActors.as_view()),
   path('ViewReview/<str:pk>/',FilmReview.as_view()),
   path('ViewSearch/<str:pk>/',FilmSearch.as_view()),
   path('create/', FilmAdd.as_view()),
   path('update/<str:pk>/', FilmUpdate.as_view()),
   path('delete/<str:pk>/', FilmDelete.as_view()),
   path('getFilm/<str:pk>/', FilmCategories.as_view()),
]
