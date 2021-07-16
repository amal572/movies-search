from django.urls import path
from .views import InteractView,InteractAdd,InteractUpdate,InteractDelete

urlpatterns = [
   path('view/', InteractView.as_view()),
   path('create/', InteractAdd.as_view()),
   path('update/<str:pk>/', InteractUpdate.as_view()),
   path('delete/<str:pk>/', InteractDelete.as_view()),
]
