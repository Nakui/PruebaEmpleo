from task.views import TaskList, TaskCreate, TaskUpdate, TaskDelete
from django.urls import path

app_name = 'task'

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
]