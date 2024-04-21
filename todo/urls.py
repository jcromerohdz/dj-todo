from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('task_done/<int:id>/', views.task_done, name='task_done'),
    path('task_undone/<int:id>/', views.task_undone, name='task_undone'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),

]