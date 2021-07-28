from django.urls import path
from .views import CategoriesFilmAdd,CategoriesFilmDelete,CategoriesFilmUpdate,CategoriesFilmView

urlpatterns = [
   path('view/', CategoriesFilmView.as_view()),
   path('create/', CategoriesFilmAdd.as_view()),
   path('update/<str:pk>/', CategoriesFilmUpdate.as_view()),
   path('delete/<str:pk>/', CategoriesFilmDelete.as_view()),
]