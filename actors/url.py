from django.urls import path
from .views import ActorsView, ActorsViewDetail, ActorsAdd ,ActorsUpdate ,ActorsDelete

urlpatterns = [
   path('view/', ActorsView.as_view()),
   path('viewDetail/', ActorsViewDetail.as_view()),
   path('create/', ActorsAdd.as_view()),
   path('update/<str:pk>/', ActorsUpdate.as_view()),
   path('delete/<str:pk>/', ActorsDelete.as_view()),
]
