from django.urls import path

from cats.views import CatList, CatDetial

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetial.as_view()),
]
