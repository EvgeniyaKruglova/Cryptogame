from django.urls import path
from .views import (
    main_page, task_detail,task_list, task_create, task_edit, task_delete, PartnerList, PartnerDetail
)

urlpatterns = [
    path('', main_page, name='main_page'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('tasklist', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('', PartnerList.as_view()),
    path('<int:pk>', PartnerDetail.as_view()),
]