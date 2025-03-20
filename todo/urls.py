from django.urls import path
from .views import task_list, delete_task, toggle_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
]
