from django.urls import path
from .views import (
    main_page,TaskList,TaskDetail, TaskCreate, TaskEdit, TaskDelete, PartnerList, PartnerDetail, ProfileDetail
)

urlpatterns = [
    path('', main_page, name='main_page'),
    path('tasklist', TaskList.as_view, name='task_list'),
    path('tasklist/<int:pk>', TaskDetail.as_view, name='task_detail'),
    path('tasklist/create/', TaskCreate.as_view, name='task_create'),
    path('tasklist/<int:pk>/edit/', TaskEdit.as_view, name='task_edit'),
    path('tasklist/<int:pk>/delete/', TaskDelete.as_view, name='task_delete'),
    path('', PartnerList.as_view()),
    path('<int:pk>', PartnerDetail.as_view()),
    path('<int:pk>', ProfileDetail.as_view()),
]