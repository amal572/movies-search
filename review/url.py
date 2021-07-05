from django.urls import path
from .views import ReviewView,ReviewAdd,ReviewUpdate,ReviewDelete

urlpatterns = [
   path('view/', ReviewView.as_view()),
   path('create/', ReviewAdd.as_view()),
   path('update/<str:pk>/', ReviewUpdate.as_view()),
   path('delete/<str:pk>/', ReviewDelete.as_view()),
]
