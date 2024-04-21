from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


# Create your views here.
def addTask(request):
    print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')

def task_done(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()

    return redirect('home')
    
def task_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()

    return redirect('home')

def edit_task(request, id):
    get_task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)