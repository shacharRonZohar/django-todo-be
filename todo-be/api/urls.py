from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview),
    path('todos/', views.get_todo_list),
    path('create/', views.create_todo)
]
