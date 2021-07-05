from django.urls import path
from .views import CategoriesView,CategoriesViewDetail,CategoriesAdd,CategoriesUpdate,CategoriesDelete

urlpatterns = [
   path('view/', CategoriesView.as_view()),
   path('viewDetail/', CategoriesViewDetail.as_view()),
   path('create/' ,CategoriesAdd.as_view()),
   path('update/<str:pk>/' ,CategoriesUpdate.as_view()),
   path('delete/<str:pk>/' ,CategoriesDelete.as_view()),
]
