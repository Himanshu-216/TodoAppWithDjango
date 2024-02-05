from django.urls import path
from .views import TaskDetail, CreateTask, TaskList, TaskUpdate, DeleteView, CustomLoginView, logout_user, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_user, name = "logout"),
    path('register/', RegisterPage.as_view(), name= 'register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task', CreateTask.as_view(), name='task-create'),
    path('task-delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
]