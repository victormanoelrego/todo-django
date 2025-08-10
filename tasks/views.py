from django.views.generic import ListView, DetailView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
