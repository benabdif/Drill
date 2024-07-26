# tasks/views.py
from django.shortcuts import render, redirect
from .models import Task, GroupWorkshop, Employee
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, GroupWorkshopForm

@login_required
def dashboard(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    elif request.user.employee.position == 'Supervisor':
        tasks = Task.objects.filter(assigned_by=request.user)
    else:
        tasks = Task.objects.filter(assigned_to=request.user.employee)
    return render(request, 'blog/dashboard.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'blog/add_task.html', {'form': form})

@login_required
def add_group_workshop(request):
    if request.method == 'POST':
        form = GroupWorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GroupWorkshopForm()
    return render(request, 'blog/add_group_workshop.html', {'form': form})


def main_page(request):
    context = {
        'fadhel': 'Hello from Fadhel'
    }
    return render(request, 'blog/mainpage.html', context)