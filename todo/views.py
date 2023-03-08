from django.shortcuts import render
from .forms import TaskForm
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here
@login_required(login_url="login")
def all(request):
    tasks = Task.objects.all()
    context = {}
    context['tasks'] = tasks.filter(user=request.user)
    context['count'] = context['tasks'].filter(completed=False).count()
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['tasks'] = context['tasks'].filter(title__icontains = search_input)
        context['search_input'] = search_input
    context['type'] = 'all'
    return render(request,'todo/todo.html',context)

@login_required(login_url="login")
def active(request):
    tasks = Task.objects.filter(completed=False)
    context = {}
    context['tasks'] = tasks.filter(user=request.user)
    context['count'] = context['tasks'].filter(completed=False).count()
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['tasks'] = context['tasks'].filter(title__icontains = search_input)
        context['search_input'] = search_input
    context['type'] = 'active'
    return render(request,'todo/todo.html',context)

@login_required(login_url="login")
def completed(request):
    tasks = Task.objects.filter(completed=True)
    context = {}
    context['tasks'] = tasks.filter(user=request.user)
    context['count'] = Task.objects.filter(user=request.user).filter(completed=False).count()
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['tasks'] = context['tasks'].filter(title__icontains = search_input)
        context['search_input'] = search_input
    context['type'] = 'completed'
    return render(request,'todo/todo.html',context)

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task    
    form_class = TaskForm
    login_url = 'login'
    success_url = reverse_lazy('all')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    login_url = 'login'
    context_object_name = 'task'
    template_name = 'todo/task.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    login_url = 'login'
    form_class = TaskForm
    success_url = reverse_lazy('all')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    login_url = 'login'
    context_object_name = 'task'
    success_url = reverse_lazy('all')
