from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.getTodoList),
    path('create/', views.createTodo)
]
