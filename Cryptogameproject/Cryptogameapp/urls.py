from django.urls import path, include
from .views import (
    main_page, TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete, PartnerList, PartnerDetail, ProfileDetail,
    ProfileAPIView, TasckCardAPIView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileAPIView)
router.register(r'taskcard', TasckCardAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', main_page, name='main_page'),
    path('tasklist', TaskList.as_view, name='task_list'),
    path('tasklist/<int:pk>', TaskDetail.as_view, name='task_detail'),
    path('tasklist/create/', TaskCreate.as_view, name='task_create'),
    path('tasklist/<int:pk>/edit/', TaskEdit.as_view, name='task_edit'),
    path('tasklist/<int:pk>/delete/', TaskDelete.as_view, name='task_delete'),
    path('patners', PartnerList.as_view()),
    path('patners/<int:pk>', PartnerDetail.as_view()),
    path('<int:pk>', ProfileDetail.as_view()),
]