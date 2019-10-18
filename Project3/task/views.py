from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task.forms import TaskForm
from task.models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'task/task_list.html'
    paginate_by = 3


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')

class TaskDelete(DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task:task_list')