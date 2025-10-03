from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('profile/create_task/', views.create_task, name='create_task'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_task/<task_id>/', views.edit_task, name='edit_task'),
    path('profile/delete_task/<task_id>/', views.delete_task, name='delete_task'),
    path('login/', views.user_login, name='login'),
]