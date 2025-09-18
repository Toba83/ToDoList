from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('tasks/', views.Task_list, name='task_list'),
    path('tasks/<int:pk>/', views.Task_detail, name='task_detail'),
]