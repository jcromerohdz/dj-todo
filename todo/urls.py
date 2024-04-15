from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('task_done/<int:id>/', views.task_done, name='task_done'),

]