from django.urls import path
from .views import main_page, task_list, task_create

urlpatterns = [
    path('', main_page, name='main_page'),
    path('tasklist', task_list, name='task_list'),
    path('create/', task_create, name='task_create')

]