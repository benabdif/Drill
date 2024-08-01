# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, GroupWorkshop, Employee, Manager, Supervisor, Employee_2
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, GroupWorkshopForm

# @login_required
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




def createTask(request):
    supervisor = get_object_or_404(Supervisor, user=request.user)
    context = {
        "supervisor": supervisor
    }

    return render(request, 'blog/createTask.html', context)



def createTask1(request):
    manager = get_object_or_404(Manager, user=request.user)
    context = {
        "manager": manager
    }

    return render(request, 'blog/createTask.html', context)


def createTask2(request):
    employee_2 = get_object_or_404(Employee_2, user=request.user)
    context = {
        "employee_2": employee_2 
    }
  
    return render(request, 'blog/createTask.html', context)



