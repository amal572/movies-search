from django.urls import path
from .views import ReviewView,ReviewAdd,ReviewUpdate,ReviewDelete,Add,AddToDatabase

urlpatterns = [
   path('view/', ReviewView.as_view()),
   path('create/', Add.as_view()),
   path('update/<str:pk>/', ReviewUpdate.as_view()),
   path('delete/<str:pk>/', ReviewDelete.as_view()),
   path('add-to-database/', AddToDatabase.as_view()),
]
