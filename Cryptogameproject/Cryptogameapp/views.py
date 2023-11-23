from django.shortcuts import render, redirect
from rest_framework import filters
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from . import tweepy
from .models import StudyCard, TaskCard, Partner, Profile
from .forms import TaskForm
from .filters import  TaskCardFilter
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .tweepy import api


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

@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        task_list = TaskCard.objects.all()
        serializer = TaskCardSerializer(task_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def task_list(request):
#     tasks = TaskCardFilter(request.GET, queryset=TaskCard.objects.all())
#     return render(
#         request,
#         'task_list.html',
#         context={'tasks': tasks})

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


def task_update(request,**kwargs):

    username = Profile.twitter_username
    try:
        user = api.get_user(screen_name=username)
        user_id = user.id
        print(f'User ID for {username} is: {user_id}')
    except tweepy.error.TweepError as e:
        print(f'Error: {e}')
    return user_id
    categoty_task = TaskCard.category
    if categoty_task == "LK":
        response = client.get_liked_tweets(user_id, tweet_fields=["created_at"])

        for tweet in response.data:
            return tweet.id, tweet.created_at
        tweet.id.save()
        tweet.created_at.save()
        print(tweet.id)
    else:
        query = "CRYPTOCAPS"
        tweets = api.search(q=query)
        for tweet in tweets:
           return tweet.text
        tweet.text.save()
        print(tweet.text)

    task_card = TaskCard.objects.get(id=kwargs.get('pk'))
    task_card.progress = 'CM'
    task_card.save()
class PartnerList(ListView):
    model = Partner
    ordering = 'name'
    template_name = 'partners.html'
    context_object_name = 'partners'

class PartnerDetail(DetailView):
    model = Partner
    template_name = 'partner.html'
    context_object_name = 'partner'
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
