from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect

tasks = []

completed_tasks = []

def tasks_view(request):
    return render(request,"tasks.html", {"tasks": tasks}) 

def completed_tasks_view(request):
    return render(request,"completed.html", {"tasks": completed_tasks}) 

def add_task_view(request):
    task_val = request.GET.get("task")
    tasks.append(task_val)
    return HttpResponseRedirect("/tasks") 

def delete_task_view(request, idx):
    tasks.pop(idx-1)
    return HttpResponseRedirect("/tasks") 

def complete_task_view(request, idx):
    completed_tasks.append(tasks.pop(idx-1))
    return HttpResponseRedirect("/tasks") 

def all_tasks_view(request):
    return render(request,"all_tasks.html", {"pending": tasks, "completed": completed_tasks}) 

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("tasks/", tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:idx>/", delete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("complete_task/<int:idx>/", complete_task_view),
    path("all_tasks/", all_tasks_view)
]
