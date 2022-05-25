from django.urls import path
from .api import TaskList, TaskDetail
from .views import TaskListView

urlpatterns = [

    path('tasks/',TaskList.as_view()),
    path('tasks/<int:pk>',TaskDetail.as_view()),

    path('taskl/',TaskListView.as_view())
]