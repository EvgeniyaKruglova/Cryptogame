from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import filters, viewsets
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .tweepy import get_twitter_user_id

from .models import StudyCard, TaskCard, Partner, Profile
from .forms import TaskForm
from .filters import  TaskCardFilter
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse


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

# @api_view(['GET','POST'])
# def task_list(request):
#     if request.method == 'GET':
#         task_list = TaskCard.objects.all()
#         serializer = TaskCardSerializer(task_list, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TaskCardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskList(ListView):
    model = TaskCard
    odering = 'published'
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TaskCardFilter (self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class TaskDetail(DetailView):
    model = TaskCard
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('Cryptogameapp.add_Task')
    form_class = TaskForm
    model = TaskCard
    template_name = 'task_edit.html'
    # def form_valid(self, form):
    #     a = form.save(commit=False)
    #     a.creator = Creator.objects.get(creator_user=self.request.user)
    #     a.save()
    #     return super().form_valid(form)


class TaskEdit (PermissionRequiredMixin,UpdateView):
    permission_required = ('Cryptogameapp.change_Task')
    form_class = TaskForm
    model = TaskCard
    template_name = 'task_edit.html'

    def dispatch(self, request, *args, **kwargs):
        creator = TaskCard.objects.get(pk=self.kwargs.get('pk')).creator.creator_user
        if self.request.user == creator:
            return super().dispatch(request, *args, **kwargs)
        else:
             return HttpResponse("Редактировать задание может только его автор")



class TaskDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('Cryptogameapp.delete_Task')
    model = TaskCard
    template_name = 'taskcard_delete.html'
    success_url = reverse_lazy('task_list')
    def dispatch(self, request, *args, **kwargs):
        creator = TaskCard.objects.get(pk=self.kwargs.get('pk')).creator.creator_user
        if self.request.user == creator:
            return super().dispatch(request, *args, **kwargs)
        else:
             return HttpResponse("Удалить задание может только его автор")





#     categoty_task = TaskCard.category
#     if categoty_task == "LK":
#         response = client.get_liked_tweets(user_id, tweet_fields=["created_at"])
#
#         for tweet in response.data:
#             return tweet.id, tweet.created_at
#         tweet.id.save()
#         tweet.created_at.save()
#         print(tweet.id)
#     else:
#         query = "CRYPTOCAPS"
#         tweets = api.search(q=query)
#         for tweet in tweets:
#            return tweet.text
#         tweet.text.save()
#         print(tweet.text)
#
#     task_card = TaskCard.objects.get(id=kwargs.get('pk'))
#     task_card.progress = 'CM'
#     task_card.save()
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
    username = Profile.twitter_username
    # user = get_twitter_user_id(username)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.user
    #     return context

class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = ProfileSerializer

class TasckCardAPIView(viewsets.ModelViewSet):
    queryset = TaskCard.objects.all().order_by('published')
    serializer_class = TaskCardSerializer

