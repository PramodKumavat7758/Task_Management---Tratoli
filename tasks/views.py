import threading
from http.client import responses

from django.db.models.expressions import result
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.TaskSerializer import TaskSerializer
from tasks.models import Task
from tasks.tasks import send_task_notification


# Create your views here.

class TaskReportAPI (APIView):
    def get(self,request):
        completed_tasks =[]
        pending_tasks =[]
        priority_cnt ={'low':0,'medium':0,'high':0}

        def fetch_data():
            tasks = Task.object.all()
            for task in tasks:
                if task.status=='completed':
                    completed_tasks.append(task)
                else:
                    pending_tasks.append(task)
                priority_cnt[task.priority] +=1

        thread = threading.Thread(target=fetch_data)
        thread.start()
        thread.join()

        return Response({
            "completed_tasks":len(completed_tasks),
            "pending_tasks":len(pending_tasks),
            "tasks_by_priority":priority_cnt
        })

def create(self, request,*args,**kwargs):
    response = super().create(request,*args,**kwargs)
    task = self.get_objec()
    send_task_notification.delay(task.assigned_to.email,task.title)
    return  response















class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
