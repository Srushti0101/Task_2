from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Task

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('tasks')
    all_tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': all_tasks})

def contact(request):
    sent = False
    if request.method == 'POST':
        # In a real project you'd save this or send an email
        sent = True
    return render(request, 'contact.html', {'sent': sent})


# --- HttpResponse views (plain text, no template) ---

def hello(request, name):
    return HttpResponse(f"Hello, {name}! Welcome to the mini project.",
                        content_type="text/plain")

def task_count(request):
    total = Task.objects.count()
    done = Task.objects.filter(completed=True).count()
    return HttpResponse(f"Total: {total}, Done: {done}, Pending: {total - done}",
                        content_type="text/plain")


# --- Template views (with a URL parameter) ---

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)   # shows a 404 page if the id doesn't exist
    return render(request, 'task_detail.html', {'task': task})


# --- Action views (POST only, then redirect back to the list) ---

@require_POST
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks')

@require_POST
def task_delete(request, task_id):
    get_object_or_404(Task, id=task_id).delete()
    return redirect('tasks')