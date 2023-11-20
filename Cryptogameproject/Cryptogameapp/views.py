from django.shortcuts import render, redirect
from rest_framework import filters
from django.core.paginator import Paginator
from .models import StudyCard, TaskCard, Partner
from .forms import TaskForm
from .filters import  TaskCardFilter
from django.views.generic import ListView, DetailView


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


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

class PartnerList(ListView):
    model = Partner
    ordering = 'name'
    template_name = 'partners.html'
    context_object_name = 'partners'

class PartnerDetail(DetailView):
    model = Partner
    template_name = 'partner.html'
    context_object_name = 'partner'

