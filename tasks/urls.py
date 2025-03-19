from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet, TaskReportAPI
from django.urls import  path, include
router = DefaultRouter()

router.register('tasks',TaskViewSet)

urlpatterns=[
    path('',include(router.urls)),

    path('report/',TaskReportAPI.as_view(),name='task_report'),
]