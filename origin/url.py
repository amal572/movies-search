from django.urls import path
from .views import OriginAdd, OriginView, OriginUpdate, OriginDelete, OriginViewDetail

urlpatterns = [
   path('view/', OriginView.as_view()),
   path('viewDetail/', OriginViewDetail.as_view()),
   path('create/', OriginAdd.as_view()),
   path('update/<str:pk>/', OriginUpdate.as_view()),
   path('delete/<str:pk>/', OriginDelete.as_view()),
]