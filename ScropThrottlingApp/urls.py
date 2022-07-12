from django.urls import path,include
from .import views



urlpatterns = [
    path('list/',views.UserList.as_view()),
    path('retrive/<int:pk>/',views.UserRetrive.as_view()),
    path('create/',views.UserCreate.as_view()),
    path('update/<int:pk>/',views.UserUpdate.as_view()),
    path('delete/<int:pk>/',views.UserDelete.as_view()),
]
