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





def dashboard1(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'blog/dashboard.html', {'tasks': tasks})






from django.shortcuts import render, redirect
from .forms import TaskForm

# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.assigned_by = request.user
#             task.save()
#             form.save_m2m()  # Only needed if there are many-to-many fields
#             return redirect('dashboard')
#     else:
#         form = TaskForm()
#     return render(request, 'blog/add_task.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'blog/add_task.html', {'form': form})




# @login_required
# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.assigned_by = request.user
#             task.save()
#             form.save_m2m()
#             return redirect('dashboard')
#     else:
#         form = TaskForm()
#     return render(request, 'blog/add_task.html', {'form': form})


# from django.shortcuts import render, redirect
# from .forms import TaskForm

# def create_task_To(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page or another view
#     else:
#         form = TaskForm()
#     return render(request, 'create_task.html', {'form': form})
















# @login_required
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
    
    return render(request, 'blog/mainpage.html')


def createTask(request):
    supervisor = Supervisor.objects.filter(user=request.user).first()
    manager = Manager.objects.filter(user=request.user).first()
    
    if not (supervisor or manager):
        return render(request, "blog/employee.html")
    
    context = {
        "supervisor": supervisor,
        "manager": manager
    }

    return render(request, 'blog/createTask.html', context)




def createTask2(request):
    employee_2 = get_object_or_404(Employee_2, user=request.user)
    context = {
        "employee_2": employee_2 
    }
  
    return render(request, 'blog/createTask.html', context)



# def myaddTask(request):
    
#     print(request.POST.get('title'))


