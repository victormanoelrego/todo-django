from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')