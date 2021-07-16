from django.urls import path
from .views import SearchView,SearchAdd,SearchUpdate,SearchDelete

urlpatterns = [
   path('view/', SearchView.as_view()),
   path('create/', SearchAdd.as_view()),
   path('update/<str:pk>/', SearchUpdate.as_view()),
   path('delete/<str:pk>/', SearchDelete.as_view()),
]
