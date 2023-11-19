from django.shortcuts import render, redirect
from rest_framework import filters
from django.core.paginator import Paginator
from .models import StudyCard, TaskCard
from .forms import TaskForm
from .filters import  TaskCardFilter
from django.shortcuts import get_object_or_404
def main_page (request):
    study = StudyCard.objects.all()
    paginator = Paginator(study,3)
    page_number = request.GET.get("page")
    page_obj_1 = paginator.get_page(page_number)
    tasks = TaskCard.objects.all()
    paginator = Paginator(tasks,3)
    page_number = request.GET.get("page")
    page_obj_2 = paginator.get_page(page_number)
    return render(
        request,
        'main_page.html',
        context=
        {'study':study, 'tasks':tasks, 'page_obj-1': page_obj_1,'page_obj-2': page_obj_2}

    )


def task_list(request):
    tasks = TaskCardFilter(request.GET, queryset=TaskCard.objects.all())
    return render(
        request,
        'task_list.html',
        context={'tasks': tasks})

def task_detail(request,pk):
    task= get_object_or_404(TaskCard,pk=pk)
    return render(
        request,
        'task_detail.html',
        context={'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(TaskCard, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(TaskCard, pk=pk)
    task.delete()
    return redirect('task_list')
