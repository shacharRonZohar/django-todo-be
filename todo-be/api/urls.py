from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TodoView),
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
]
