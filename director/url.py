from django.urls import path
from .views import DirectorAdd,DirectorDelete,DirectorView,DirectorUpdate,DirectorViewDetail

urlpatterns = [
   path('view/', DirectorView.as_view()),
   path('viewDetail/', DirectorViewDetail.as_view()),
   path('create/', DirectorAdd.as_view()),
   path('update/<str:pk>/', DirectorUpdate.as_view()),
   path('delete/<str:pk>/', DirectorDelete.as_view()),
]