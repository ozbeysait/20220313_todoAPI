from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskDeleteAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='tasks'),
    path('tasks/<pk>/', TaskDetailAPIView.as_view(), name='task'),
    path('create/', TaskCreateAPIView.as_view(), name='create'),
    path('update/<pk>/', TaskUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>/', TaskDeleteAPIView.as_view(), name='delete'),
]